# Generated by Django 2.0.3 on 2018-04-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20180425_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvester',
            name='metadataPrefix',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
