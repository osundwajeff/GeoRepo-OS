# Generated by Django 4.0.7 on 2023-03-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('georepo', '0077_datasetviewresource_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='geographicalentity',
            name='privacy_level',
            field=models.IntegerField(default=4),
        ),
    ]
