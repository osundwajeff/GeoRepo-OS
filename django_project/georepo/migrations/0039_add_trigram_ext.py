# Generated by Django 4.0.7 on 2022-12-02 01:40

from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension


class Migration(migrations.Migration):

    dependencies = [
        ('georepo', '0038_datasetview_bbox_datasetview_description_and_more'),
    ]

    operations = [
        TrigramExtension()
    ]
