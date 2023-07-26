# Generated by Django 4.0.7 on 2023-07-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('georepo', '0099_remove_entitysimplified_max_zoom_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetview',
            name='simplification_progress',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datasetview',
            name='simplification_task_id',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]
