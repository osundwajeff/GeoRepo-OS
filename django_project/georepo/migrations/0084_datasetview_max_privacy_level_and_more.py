# Generated by Django 4.0.7 on 2023-03-12 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('georepo', '0083_datasetviewresource_bbox'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetview',
            name='max_privacy_level',
            field=models.IntegerField(default=4, help_text='updated when view is refreshed'),
        ),
        migrations.AddField(
            model_name='datasetview',
            name='min_privacy_level',
            field=models.IntegerField(default=4, help_text='updated when view is refreshed'),
        ),
    ]
