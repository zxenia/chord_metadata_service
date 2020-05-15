# Generated by Django 2.2.12 on 2020-05-13 18:01

import chord_metadata_service.restapi.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0004_auto_20200401_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='biosample',
            field=models.ForeignKey(blank=True, help_text='Biosample on which this experiment was done', null=True, on_delete=django.db.models.deletion.SET_NULL, to='phenopackets.Biosample'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='experiment_ontology',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='(Ontology: OBI) links to experiment ontology information.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_list_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'description': 'Ontology class list', 'items': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'todo', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'title': 'Ontology class list', 'type': 'array'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='molecule_ontology',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='(Ontology: SO) links to molecule ontology information.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_list_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'description': 'Ontology class list', 'items': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'todo', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'title': 'Ontology class list', 'type': 'array'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='other_fields',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='The other fields for the experiment', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:key_value_object_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'The schema represents a key-value object.', 'patternProperties': {'^.*$': {'type': 'string'}}, 'title': 'Key-value object', 'type': 'object'}, formats=None)]),
        ),
    ]
