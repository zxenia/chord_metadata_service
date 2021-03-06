# Generated by Django 2.2.12 on 2020-05-19 15:38

import chord_metadata_service.restapi.validators
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chord', '0013_table'),
        ('phenopackets', '0010_auto_20200515_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phenopacket',
            name='dataset',
        ),
        migrations.AddField(
            model_name='phenopacket',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chord.Table'),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='diagnostic_markers',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='A list of ontology terms representing clinically-relevant bio-markers.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_list_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'description': 'Ontology class list', 'items': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ontology term.', 'help': 'An ontology term.', 'properties': {'id': {'description': 'A CURIE-style identifier for an ontology term.', 'help': 'A CURIE-style identifier for an ontology term.', 'type': 'string'}, 'label': {'description': 'A human readable class name for an ontology term.', 'help': 'A human readable class name for an ontology term.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'title': 'Ontology class list', 'type': 'array'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='histological_diagnosis',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology term representing a refinement of the clinical diagnosis. Normal samples could be tagged with NCIT:C38757, representing a negative finding.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ontology term.', 'help': 'An ontology term.', 'properties': {'id': {'description': 'A CURIE-style identifier for an ontology term.', 'help': 'A CURIE-style identifier for an ontology term.', 'type': 'string'}, 'label': {'description': 'A human readable class name for an ontology term.', 'help': 'A human readable class name for an ontology term.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='sampled_tissue',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='An ontology term describing the tissue from which the specimen was collected. The use of UBERON is recommended.', validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ontology term.', 'help': 'An ontology term.', 'properties': {'id': {'description': 'A CURIE-style identifier for an ontology term.', 'help': 'A CURIE-style identifier for an ontology term.', 'type': 'string'}, 'label': {'description': 'A human readable class name for an ontology term.', 'help': 'A human readable class name for an ontology term.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='taxonomy',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology term specified when more than one organism may be studied. It is advised that codesfrom the NCBI Taxonomy resource are used, e.g. NCBITaxon:9606 for humans.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ontology term.', 'help': 'An ontology term.', 'properties': {'id': {'description': 'A CURIE-style identifier for an ontology term.', 'help': 'A CURIE-style identifier for an ontology term.', 'type': 'string'}, 'label': {'description': 'A human readable class name for an ontology term.', 'help': 'A human readable class name for an ontology term.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='tumor_grade',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology term representing the tumour grade. This should be a child term of NCIT:C28076 (Disease Grade Qualifier) or equivalent.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ontology term.', 'help': 'An ontology term.', 'properties': {'id': {'description': 'A CURIE-style identifier for an ontology term.', 'help': 'A CURIE-style identifier for an ontology term.', 'type': 'string'}, 'label': {'description': 'A human readable class name for an ontology term.', 'help': 'A human readable class name for an ontology term.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='tumor_progression',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology term representing if the specimen is from a primary tumour, a metastasis, or a recurrence. There are multiple ways of representing this using ontology terms, and the terms chosen will have a specific meaning that is application specific.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ontology term.', 'help': 'An ontology term.', 'properties': {'id': {'description': 'A CURIE-style identifier for an ontology term.', 'help': 'A CURIE-style identifier for an ontology term.', 'type': 'string'}, 'label': {'description': 'A human readable class name for an ontology term.', 'help': 'A human readable class name for an ontology term.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='disease',
            name='disease_stage',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='A list of terms representing the disease stage. Elements should be derived from child terms of NCIT:C28108 (Disease Stage Qualifier) or equivalent hierarchy from another ontology.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_list_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'description': 'Ontology class list', 'items': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ontology term.', 'help': 'An ontology term.', 'properties': {'id': {'description': 'A CURIE-style identifier for an ontology term.', 'help': 'A CURIE-style identifier for an ontology term.', 'type': 'string'}, 'label': {'description': 'A human readable class name for an ontology term.', 'help': 'A human readable class name for an ontology term.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'title': 'Ontology class list', 'type': 'array'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='disease',
            name='term',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text="An ontology term that represents the disease. It's recommended that one of the OMIM, Orphanet, or MONDO ontologies is used for rare human diseases.", validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ontology term.', 'help': 'An ontology term.', 'properties': {'id': {'description': 'A CURIE-style identifier for an ontology term.', 'help': 'A CURIE-style identifier for an ontology term.', 'type': 'string'}, 'label': {'description': 'A human readable class name for an ontology term.', 'help': 'A human readable class name for an ontology term.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='disease',
            name='tnm_finding',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='A list of terms representing the tumour TNM score. Elements should be derived from child terms of NCIT:C48232 (Cancer TNM Finding) or equivalent hierarchy from another ontology.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_list_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'description': 'Ontology class list', 'items': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ontology term.', 'help': 'An ontology term.', 'properties': {'id': {'description': 'A CURIE-style identifier for an ontology term.', 'help': 'A CURIE-style identifier for an ontology term.', 'type': 'string'}, 'label': {'description': 'A human readable class name for an ontology term.', 'help': 'A human readable class name for an ontology term.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'title': 'Ontology class list', 'type': 'array'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='gene',
            name='alternate_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), blank=True, default=list, help_text='A list of identifiers for alternative resources where the gene is used or catalogued.', size=None),
        ),
        migrations.AlterField(
            model_name='phenotypicfeature',
            name='modifier',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='A list of ontology terms that provide more expressive / precise descriptions of a phenotypic feature, including e.g. positionality or external factors.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_list_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'description': 'Ontology class list', 'items': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ontology term.', 'help': 'An ontology term.', 'properties': {'id': {'description': 'A CURIE-style identifier for an ontology term.', 'help': 'A CURIE-style identifier for an ontology term.', 'type': 'string'}, 'label': {'description': 'A human readable class name for an ontology term.', 'help': 'A human readable class name for an ontology term.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'title': 'Ontology class list', 'type': 'array'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='phenotypicfeature',
            name='onset',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology term that describes the age at which the phenotypic feature was first noticed or diagnosed, e.g. HP:0003674.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ontology term.', 'help': 'An ontology term.', 'properties': {'id': {'description': 'A CURIE-style identifier for an ontology term.', 'help': 'A CURIE-style identifier for an ontology term.', 'type': 'string'}, 'label': {'description': 'A human readable class name for an ontology term.', 'help': 'A human readable class name for an ontology term.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='phenotypicfeature',
            name='pftype',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='An ontology term which describes the phenotype.', validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ontology term.', 'help': 'An ontology term.', 'properties': {'id': {'description': 'A CURIE-style identifier for an ontology term.', 'help': 'A CURIE-style identifier for an ontology term.', 'type': 'string'}, 'label': {'description': 'A human readable class name for an ontology term.', 'help': 'A human readable class name for an ontology term.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)], verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='phenotypicfeature',
            name='severity',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology term that describes the severity of the condition.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ontology term.', 'help': 'An ontology term.', 'properties': {'id': {'description': 'A CURIE-style identifier for an ontology term.', 'help': 'A CURIE-style identifier for an ontology term.', 'type': 'string'}, 'label': {'description': 'A human readable class name for an ontology term.', 'help': 'A human readable class name for an ontology term.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='body_site',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology term that is specified when it is not possible to represent the procedure with a single ontology class.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ontology term.', 'help': 'An ontology term.', 'properties': {'id': {'description': 'A CURIE-style identifier for an ontology term.', 'help': 'A CURIE-style identifier for an ontology term.', 'type': 'string'}, 'label': {'description': 'A human readable class name for an ontology term.', 'help': 'A human readable class name for an ontology term.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='code',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='An ontology term that represents a clinical procedure performed on a subject.', validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ontology term.', 'help': 'An ontology term.', 'properties': {'id': {'description': 'A CURIE-style identifier for an ontology term.', 'help': 'A CURIE-style identifier for an ontology term.', 'type': 'string'}, 'label': {'description': 'A human readable class name for an ontology term.', 'help': 'A human readable class name for an ontology term.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='variant',
            name='zygosity',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology term taken from the Genotype Ontology (GENO) representing the zygosity of the variant.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ontology term.', 'help': 'An ontology term.', 'properties': {'id': {'description': 'A CURIE-style identifier for an ontology term.', 'help': 'A CURIE-style identifier for an ontology term.', 'type': 'string'}, 'label': {'description': 'A human readable class name for an ontology term.', 'help': 'A human readable class name for an ontology term.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
    ]
