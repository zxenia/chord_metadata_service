# Generated by Django 2.2.9 on 2020-01-28 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chord', '0005_auto_20200123_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='contact_info',
            field=models.TextField(blank=True),
        ),
    ]