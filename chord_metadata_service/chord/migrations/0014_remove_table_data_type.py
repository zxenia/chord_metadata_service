# Generated by Django 2.2.12 on 2020-05-19 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chord', '0013_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='data_type',
        ),
    ]
