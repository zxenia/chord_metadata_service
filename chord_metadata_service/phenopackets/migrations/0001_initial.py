# Generated by Django 2.2.8 on 2019-12-10 21:04

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        ('chord', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biosample',
            fields=[
                ('id', models.CharField(help_text='An arbitrary identifier.', max_length=200, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, help_text='The biosample’s description.', max_length=200)),
                ('sampled_tissue', django.contrib.postgres.fields.jsonb.JSONField(help_text='An Ontology term describing the tissue from which the sample was taken.')),
                ('taxonomy', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An Ontology term describing the species of the sampled individual.', null=True)),
                ('individual_age_at_collection', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Age of the proband at the time the sample was taken.', null=True)),
                ('histological_diagnosis', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An Ontology term describing the disease diagnosis that was inferred from the histological examination.', null=True)),
                ('tumor_progression', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An Ontology term describing primary, metastatic, recurrent.', null=True)),
                ('tumor_grade', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An Ontology term describing the tumor grade. Potentially a child term of NCIT:C28076 or equivalent.', null=True)),
                ('diagnostic_markers', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, help_text='List of Ontology terms describing clinically relevant biomarkers.', null=True, size=None)),
                ('is_control_sample', models.BooleanField(default=False, help_text='Whether the sample is being used as a normal control.')),
                ('extra_properties', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema', null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_properties', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema', null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', django.contrib.postgres.fields.jsonb.JSONField(help_text='An ontology term that represents the disease.')),
                ('onset', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An element representing the age of onset of the disease.', null=True)),
                ('disease_stage', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, help_text='List of terms representing the disease stage.', null=True, size=None)),
                ('tnm_finding', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, help_text='List of terms representing the tumor TNM score.', null=True, size=None)),
                ('extra_properties', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema', null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.CharField(help_text='Official identifier of the gene.', max_length=200, primary_key=True, serialize=False)),
                ('alternate_ids', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), blank=True, help_text='Alternative identifier(s) of the gene.', null=True, size=None)),
                ('symbol', models.CharField(help_text='Official gene symbol.', max_length=200)),
                ('extra_properties', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema', null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HtsFile',
            fields=[
                ('uri', models.URLField(help_text='A valid URI for the file.', primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, help_text='An arbitrary description of the file contents.', max_length=200)),
                ('hts_format', models.CharField(choices=[('UNKNOWN', 'UNKNOWN'), ('SAM', 'SAM'), ('BAM', 'BAM'), ('CRAM', 'CRAM'), ('VCF', 'VCF'), ('BCF', 'BCF'), ('GVCF', 'GVCF')], help_text='A format of the file.', max_length=200)),
                ('genome_assembly', models.CharField(help_text='The genome assembly the contents of this file was called against.', max_length=200)),
                ('individual_to_sample_identifiers', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='The mapping between the Individual.id or Biosample.id to the sample identifier in the HTS file', null=True)),
                ('extra_properties', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema', null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='Time when this object was created.')),
                ('created_by', models.CharField(help_text='Name of person who created the phenopacket.', max_length=200)),
                ('submitted_by', models.CharField(blank=True, help_text='Name of person who submitted the phenopacket.', max_length=200)),
                ('updates', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, help_text='List of updates to the phenopacket.', null=True, size=None)),
                ('phenopacket_schema_version', models.CharField(blank=True, help_text='Schema version of the current phenopacket.', max_length=200)),
                ('external_references', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, help_text='List of external resources from the phenopacket was derived.', null=True, size=None)),
                ('extra_properties', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema', null=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phenopacket',
            fields=[
                ('id', models.CharField(help_text='An arbitrary identifier for the phenopacket.', max_length=200, primary_key=True, serialize=False)),
                ('extra_properties', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema', null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('biosamples', models.ManyToManyField(blank=True, help_text='The biosamples that have been derived from an individual who is the subject of the Phenopacket. Rr a collection of biosamples in isolation.', to='phenopackets.Biosample')),
                ('dataset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chord.Dataset')),
                ('diseases', models.ManyToManyField(blank=True, help_text='Disease(s) diagnosed in the proband.', to='phenopackets.Disease')),
                ('genes', models.ManyToManyField(blank=True, help_text='Gene deemed to be relevant to the case.', to='phenopackets.Gene')),
                ('hts_files', models.ManyToManyField(blank=True, help_text='VCF or other high-throughput sequencing files.', to='phenopackets.HtsFile')),
                ('meta_data', models.ForeignKey(help_text='Information about ontologies and references used in the phenopacket.', on_delete=django.db.models.deletion.CASCADE, to='phenopackets.MetaData')),
                ('subject', models.ForeignKey(help_text='The proband.', on_delete=django.db.models.deletion.CASCADE, related_name='phenopackets', to='patients.Individual')),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', django.contrib.postgres.fields.jsonb.JSONField(help_text='Clinical procedure performed on a subject.')),
                ('body_site', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Specific body site if unable to represent this is the code.', null=True)),
                ('extra_properties', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema', null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.CharField(help_text='For OBO ontologies, the value of this string MUST always be the official OBO ID, which is always equivalent to the ID prefix in lower case. For other resources use the prefix in identifiers.org.', max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='The full name of the ontology referred to by the id element.', max_length=200)),
                ('namespace_prefix', models.CharField(help_text='The prefix used in the CURIE of an Ontology term.', max_length=200)),
                ('url', models.URLField(help_text='For OBO ontologies, this MUST be the PURL. Other resources should link to the official or top-level url.')),
                ('version', models.CharField(help_text='The version of the resource or ontology used to make the annotation.', max_length=200)),
                ('iri_prefix', models.URLField(help_text='The full IRI prefix which can be used with the namespace_prefix and the Ontology::id to resolve to an IRI for a term.')),
                ('extra_properties', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema', null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allele_type', models.CharField(choices=[('hgvsAllele', 'hgvsAllele'), ('vcfAllele', 'vcfAllele'), ('spdiAllele', 'spdiAllele'), ('iscnAllele', 'iscnAllele')], help_text='One of four allele types.', max_length=200)),
                ('allele', django.contrib.postgres.fields.jsonb.JSONField()),
                ('zygosity', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Genotype Ontology (GENO) term representing  the zygosity of the variant.', null=True)),
                ('extra_properties', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema', null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhenotypicFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, help_text='Human-readable verbiage NOT for structured text', max_length=200)),
                ('pftype', django.contrib.postgres.fields.jsonb.JSONField(help_text='Ontology term that describes the phenotype.', verbose_name='type')),
                ('negated', models.BooleanField(default=False, help_text='This element is a flag to indicate whether the phenotype was observed or not.')),
                ('severity', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Description of the severity of the featurerepresented by a term from HP:0012824.', null=True)),
                ('modifier', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, help_text='This element is  intended to provide more expressive or precise descriptions of a phenotypic feature, including attributes such as positionality and external factors that tend to trigger or ameliorate the feature.', null=True, size=None)),
                ('onset', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='This element can be used to describe the age at which a phenotypic feature was first noticed or diagnosed.', null=True)),
                ('evidence', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='This element intends to represent the evidence for an assertion such as an observation of a PhenotypicFeature.', null=True)),
                ('extra_properties', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema', null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('biosample', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phenotypic_features', to='phenopackets.Biosample')),
                ('phenopacket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phenotypic_features', to='phenopackets.Phenopacket')),
            ],
        ),
        migrations.AddField(
            model_name='phenopacket',
            name='variants',
            field=models.ManyToManyField(blank=True, help_text='Variants identified in the proband.', to='phenopackets.Variant'),
        ),
        migrations.AddField(
            model_name='metadata',
            name='resources',
            field=models.ManyToManyField(help_text='This element contains a listing of the ontologies/resources referenced in the phenopacket.', to='phenopackets.Resource'),
        ),
        migrations.CreateModel(
            name='Interpretation',
            fields=[
                ('id', models.CharField(help_text='An arbitrary identifier for the interpretation.', max_length=200, primary_key=True, serialize=False)),
                ('resolution_status', models.CharField(blank=True, choices=[('UNKNOWN', 'UNKNOWN'), ('SOLVED', 'SOLVED'), ('UNSOLVED', 'UNSOLVED'), ('IN_PROGRESS', 'IN_PROGRESS')], help_text='The current status of work on the case.', max_length=200)),
                ('extra_properties', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema', null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('diagnosis', models.ManyToManyField(help_text='One or more diagnoses, if made.', to='phenopackets.Diagnosis')),
                ('meta_data', models.ForeignKey(help_text='Metadata about this interpretation.', on_delete=django.db.models.deletion.CASCADE, to='phenopackets.MetaData')),
                ('phenopacket', models.ForeignKey(help_text='The subject of this interpretation.', on_delete=django.db.models.deletion.CASCADE, related_name='interpretations', to='phenopackets.Phenopacket')),
            ],
        ),
        migrations.CreateModel(
            name='GenomicInterpretation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('UNKNOWN', 'UNKNOWN'), ('REJECTED', 'REJECTED'), ('CANDIDATE', 'CANDIDATE'), ('CAUSATIVE', 'CAUSATIVE')], help_text='How the call of this GenomicInterpretation was interpreted.', max_length=200)),
                ('extra_properties', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema', null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('gene', models.ForeignKey(blank=True, help_text='The gene contributing to the diagnosis.', null=True, on_delete=django.db.models.deletion.CASCADE, to='phenopackets.Gene')),
                ('variant', models.ForeignKey(blank=True, help_text='The variant contributing to the diagnosis.', null=True, on_delete=django.db.models.deletion.CASCADE, to='phenopackets.Variant')),
            ],
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='disease',
            field=models.ForeignKey(help_text='The diagnosed condition.', on_delete=django.db.models.deletion.CASCADE, to='phenopackets.Disease'),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='genomic_interpretations',
            field=models.ManyToManyField(blank=True, help_text='The genomic elements assessed as being responsible for the disease.', to='phenopackets.GenomicInterpretation'),
        ),
        migrations.AddField(
            model_name='biosample',
            name='hts_files',
            field=models.ManyToManyField(blank=True, help_text='List of high-throughput sequencing files derived from the biosample.', related_name='biosample_hts_files', to='phenopackets.HtsFile'),
        ),
        migrations.AddField(
            model_name='biosample',
            name='individual',
            field=models.ForeignKey(blank=True, help_text='The id of the Individual this biosample was derived from.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='biosamples', to='patients.Individual'),
        ),
        migrations.AddField(
            model_name='biosample',
            name='procedure',
            field=models.ForeignKey(help_text='The procedure used to extract the biosample.', on_delete=django.db.models.deletion.CASCADE, to='phenopackets.Procedure'),
        ),
        migrations.AddField(
            model_name='biosample',
            name='variants',
            field=models.ManyToManyField(blank=True, help_text='List of variants determined to be present in the biosample.', to='phenopackets.Variant'),
        ),
    ]
