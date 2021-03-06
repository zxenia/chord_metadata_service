# Generated by Django 2.2.12 on 2020-05-19 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chord', '0012_auto_20200515_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('ownership_record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='chord.TableOwnership')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('data_type', models.CharField(choices=[('experiment', 'experiment'), ('phenopacket', 'phenopacket')], max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
