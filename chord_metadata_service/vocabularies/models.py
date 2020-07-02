from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.functional import cached_property
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

VOCABULARIES_SETTINGS = {
    "default_language": "en",
    "default_namespace": "https://example.org/"
}

try:
    DEFAULT_LANG = VOCABULARIES_SETTINGS['default_lang']
except KeyError:
    DEFAULT_LANG = "en"

try:
    DEFAULT_NAMESPACE = VOCABULARIES_SETTINGS['default_namespace']
except KeyError:
    DEFAULT_NAMESPACE = "https://example.org/"


class SkosConceptScheme(models.Model):
    title = models.CharField(max_length=300, verbose_name="dc:title", help_text="Title  for new concept scheme")
    title_lang = models.CharField(max_length=3, blank=True, verbose_name="dc:title language", default=DEFAULT_LANG,
                                  help_text="Language of title given above")
    identifier = models.URLField(blank=True, help_text="URI to unambiguously identify current Concept Scheme")
    creator = models.TextField(blank=True, verbose_name="dc:creator", help_text="Person or organisation primarily "
                                                                                "responsible for making current concept scheme.")
    contributor = models.TextField(blank=True, verbose_name="dc:contributor",
                                   help_text="Person or organisation that made contributions to the vocabulary.")
    language = models.TextField(blank=True, verbose_name="dc:language", help_text="Language(s) used in concept scheme.")
    subject = models.TextField(blank=True, verbose_name="dc:subject", help_text="The subject of the vocabulary.")
    version = models.CharField(max_length=300, blank=True, help_text="Current version.")
    publisher = models.CharField(max_length=300, blank=True, verbose_name="dc:publisher",
                                 help_text="Organisation responsible for making the vocabulary available")
    license = models.CharField(max_length=300, blank=True, verbose_name="dct:license",
                               help_text="Information about license applied to the vocabulary.")
    owner = models.CharField(max_length=300, blank=True, help_text="Person or organisation that owns the rights "
                                                                   "for the vocabulary.")
    relation = models.URLField(blank=True, verbose_name="dc:relation", help_text="Related resource or project. "
                                                                                 "E.g. in case of relation to a project, add link to a project website.")
    coverage = models.TextField(blank=True, verbose_name="dc:coverage", help_text="Spatial or temporal frame that "
                                                                                  "the vocabulary relates to.")
    legacy_id = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    date_issued = models.DateField(blank=True, null=True,
                                   help_text="Date of official publication of this concept scheme.")
    created_by = models.ForeignKey(User, related_name="skos_cs_created", blank=True, null=True,
                                   on_delete=models.SET_NULL)
    curator = models.ManyToManyField(User, related_name="skos_cs_curated", blank=True,
                                     help_text="The selected user(s) will be able to view and edit this Concept Scheme.")

    class Meta:
        ordering = ['id']
        verbose_name = 'Concept Scheme'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.identifier:
            self.identifier = DEFAULT_NAMESPACE + slugify(self.title, allow_unicode=True)
        super(SkosConceptScheme, self).save(*args, **kwargs)


class SkosCollection(models.Model):
    name = models.CharField(max_length=300, verbose_name="skos:prefLabel", help_text="Collection label or name.")
    label_lang = models.CharField(max_length=3, blank=True, verbose_name="skos:prefLabel language",
                                  default=DEFAULT_LANG, help_text="Language of preferred label given above.")
    # relation to SkosConceptScheme to inherit all objects permissions
    scheme = models.ForeignKey(SkosConceptScheme, related_name="has_collections", verbose_name="skos:ConceptScheme",
                               help_text="Concept scheme that this collection belongs to.", on_delete=models.CASCADE)
    creator = models.TextField(blank=True, verbose_name="dc:creator",
                               help_text="Person or organisation that created this collection.")
    contributor = models.TextField(blank=True, verbose_name="dc:contributor",
                                   help_text="Person or organisation that made contributions to the collection.")
    legacy_id = models.CharField(max_length=200, blank=True)
    # meta autosaved fields
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="skos_collection_created", blank=True, null=True,
                                   on_delete=models.SET_NULL)

    class Meta:
        ordering = ['id']
        verbose_name = 'Collection'

    def __str__(self):
        return self.name


class SkosConcept(MPTTModel):
    pref_label = models.CharField(max_length=300, verbose_name="skos:prefLabel",
                                  help_text="Preferred label for concept.")
    pref_label_lang = models.CharField(max_length=3, blank=True, verbose_name="skos:prefLabel language",
                                       help_text="Language of preferred label given above.", default=DEFAULT_LANG)
    # relation to SkosConceptScheme to inherit all objects permissions
    scheme = models.ForeignKey(SkosConceptScheme, verbose_name="skos:inScheme", related_name="has_concepts",
                               on_delete=models.CASCADE, help_text="Concept scheme to which this concept belongs.")
    top_concept = models.BooleanField(null=True, help_text="Is this concept a top concept of concept scheme?")
    collection = models.ManyToManyField(SkosCollection, blank=True, verbose_name="member of skos:Collection",
                                        help_text="Collection that this concept is a member of.",
                                        related_name="has_members")
    notation = models.CharField(max_length=300, blank=True, verbose_name="skos:notation",
                                help_text="A notation is a unique string used to identify the concept in current "
                                          "vocabulary.")
    broader_concept = TreeForeignKey('self', verbose_name="skos:broader", blank=True, null=True,
                                     on_delete=models.CASCADE, related_name="narrower_concepts",
                                     help_text="Concept with a broader meaning that this concept inherits from.")
    ################# semantic relationships via autocomplete #################
    related = models.TextField(blank=True, verbose_name="skos:related",
                               help_text="An associative relationship between two concepts.")
    broad_match = models.TextField(blank=True, verbose_name="skos:broadMatch",
                                   help_text="External concept with a broader meaning.")
    narrow_match = models.TextField(blank=True, verbose_name="skos:narrowMatch",
                                    help_text="External concept with a narrower meaning.")
    exact_match = models.TextField(blank=True, verbose_name="skos:exactMatch",
                                   help_text="External concept that can be used interchangeably and has the exact "
                                             "same meaning.")
    related_match = models.TextField(blank=True, verbose_name="skos:relatedMatch",
                                     help_text="External concept that has an associative relationship "
                                               "with this concept.")
    close_match = models.TextField(blank=True, verbose_name="skos:closeMatch",
                                   help_text="External concept that has a similar meaning.")
    ###########################################################################
    # if using legacy_id as URI change it for URLField
    legacy_id = models.CharField(max_length=200, blank=True)
    creator = models.TextField(blank=True, verbose_name="dc:creator",
                               help_text="Person or organisation that created this concept.")
    contributor = models.TextField(blank=True, verbose_name="dc:contributor",
                                   help_text="Person or organisation that made contributions to this concept.")
    needs_review = models.BooleanField(null=True, help_text="Check if this concept needs to be reviewed.")
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="skos_concept_created", blank=True, null=True,
                                   on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Concept'

    class MPTTMeta:
        order_insertion_by = ['pref_label']
        parent_attr = 'broader_concept'

    def __str__(self):
        return self.pref_label
