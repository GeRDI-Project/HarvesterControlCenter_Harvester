# Generated by Django 2.0.3 on 2018-03-23 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180323_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvester',
            name='repository',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
