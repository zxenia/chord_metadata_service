# Generated by Django 2.2.12 on 2020-05-14 19:41

import chord_metadata_service.restapi.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0008_auto_20200513_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='comorbid_condition',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='One or more conditions that occur with primary condition.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:comorbid_condition_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Comorbid condition schema.', 'properties': {'clinical_status': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'code': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}}, 'required': [], 'title': 'Comorbid Condition schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='individual',
            name='ecog_performance_status',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Value representing the Eastern Cooperative Oncology Group performance status.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='individual',
            name='karnofsky',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Value representing the Karnofsky Performance status.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='individual',
            name='taxonomy',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Ontology resource representing the species (e.g., NCBITaxon:9615).', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
    ]