# Generated by Django 2.2.9 on 2020-01-29 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_individual_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='individual',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
