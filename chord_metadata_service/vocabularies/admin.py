from django.contrib import admin
from .models import SkosConceptScheme, SkosCollection, SkosConcept
from mptt.admin import MPTTModelAdmin


@admin.register(SkosConcept)
class SkosConceptAdmin(MPTTModelAdmin):
    pass


@admin.register(SkosCollection)
class SkosCollectionAdmin(admin.ModelAdmin):
    pass


@admin.register(SkosConceptScheme)
class SkosConceptSchemeAdmin(admin.ModelAdmin):
    pass


# admin.site.register(SkosConcept, SkosConceptAdmin)
# admin.site.register(SkosCollection, SkosCollectionAdmin)
# admin.site.register(SkosConceptScheme, SkosConceptSchemeAdmin)
