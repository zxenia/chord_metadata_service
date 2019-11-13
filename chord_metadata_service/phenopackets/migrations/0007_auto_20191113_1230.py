# Generated by Django 2.2.6 on 2019-11-13 17:30

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phenopackets', '0006_auto_20191105_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='alternate_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), blank=True, help_text='Alternative identifier(s) of the gene.', null=True, size=None),
        ),
    ]
