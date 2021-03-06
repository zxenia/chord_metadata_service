# Generated by Django 2.2.12 on 2020-05-13 18:01

import chord_metadata_service.restapi.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_auto_20200430_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='age',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='The age or age range of the individual.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:age_or_age_range_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'description': 'An age object describing the age of the individual at the time of collection of biospecimens or phenotypic observations.', 'oneOf': [{'$id': 'chord_metadata_service:age_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ISO8601 duration string (e.g. P40Y10M05D for 40 years, 10 months, 5 days) representing an age of a subject.', 'help': 'An ISO8601 duration string (e.g. P40Y10M05D for 40 years, 10 months, 5 days) representing an age of a subject.', 'properties': {'age': {'description': 'An ISO8601 duration string (e.g. P40Y10M05D for 40 years, 10 months, 5 days) representing an age of a subject.', 'help': 'Age of a subject.', 'type': 'string'}}, 'required': ['age'], 'title': 'Age schema', 'type': 'object'}, {'$id': 'chord_metadata_service:age_range_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': "Age range of a subject (e.g. when a subject's age falls into a bin.)", 'help': "Age range of a subject (e.g. when a subject's age falls into a bin.)", 'properties': {'end': {'$id': 'chord_metadata_service:age_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ISO8601 duration string representing the end of the age range bin.', 'help': 'An ISO8601 duration string representing the end of the age range bin.', 'properties': {'age': {'description': 'An ISO8601 duration string (e.g. P40Y10M05D for 40 years, 10 months, 5 days) representing an age of a subject.', 'help': 'Age of a subject.', 'type': 'string'}}, 'required': ['age'], 'title': 'Age schema', 'type': 'object'}, 'start': {'$id': 'chord_metadata_service:age_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An ISO8601 duration string representing the start of the age range bin.', 'help': 'An ISO8601 duration string representing the start of the age range bin.', 'properties': {'age': {'description': 'An ISO8601 duration string (e.g. P40Y10M05D for 40 years, 10 months, 5 days) representing an age of a subject.', 'help': 'Age of a subject.', 'type': 'string'}}, 'required': ['age'], 'title': 'Age schema', 'type': 'object'}}, 'required': ['start', 'end'], 'title': 'Age range schema', 'type': 'object'}], 'title': 'Age schema', 'type': 'object'}, formats=None)]),
        ),
    ]
