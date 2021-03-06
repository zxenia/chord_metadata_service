# Generated by Django 2.2.11 on 2020-03-27 17:28

import chord_metadata_service.restapi.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='experiment_ontology',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='(Ontology: OBI) links to experiment ontology information.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'ONTOLOGY_CLASS_LIST', '$schema': 'http://json-schema.org/draft-07/schema#', 'description': 'Ontology class list', 'items': {'$id': 'ONTOLOGY_CLASS', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'todo', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'title': 'Ontology class list', 'type': 'array'})]),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='molecule',
            field=models.CharField(choices=[('total RNA', 'total RNA'), ('polyA RNA', 'polyA RNA'), ('cytoplasmic RNA', 'cytoplasmic RNA'), ('nuclear RNA', 'nuclear RNA'), ('small RNA', 'small RNA'), ('genomic DNA', 'genomic DNA'), ('protein', 'protein'), ('other', 'other')], help_text='(Controlled Vocabulary) The type of molecule that was extracted from the biological material. Include one of the following: total RNA, polyA RNA, cytoplasmic RNA, nuclear RNA, small RNA, genomic DNA, protein, or other.', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='molecule_ontology',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='(Ontology: SO) links to molecule ontology information.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'ONTOLOGY_CLASS_LIST', '$schema': 'http://json-schema.org/draft-07/schema#', 'description': 'Ontology class list', 'items': {'$id': 'ONTOLOGY_CLASS', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'todo', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'title': 'Ontology class list', 'type': 'array'})]),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='other_fields',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='The other fields for the experiment', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'KEY_VALUE_OBJECT', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'The schema represents a key-value object.', 'patternProperties': {'^.*$': {'type': 'string'}}, 'title': 'Key-value object', 'type': 'object'})]),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='reference_registry_id',
            field=models.CharField(help_text='The IHEC EpiRR ID for this dataset, only for IHEC Reference Epigenome datasets. Otherwise leave empty.', max_length=30, null=True),
        ),
    ]
