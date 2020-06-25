# Generated by Django 2.2.13 on 2020-06-18 22:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mcode', '0009_auto_20200618_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genomicsreport',
            name='issued',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='The date/time this report was issued.'),
        ),
        migrations.RemoveField(
            model_name='mcodepacket',
            name='cancer_condition',
        ),
        migrations.AddField(
            model_name='mcodepacket',
            name='cancer_condition',
            field=models.ManyToManyField(blank=True, help_text="An Individual's cancer condition.", to='mcode.CancerCondition'),
        ),
    ]
