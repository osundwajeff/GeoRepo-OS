# Generated by Django 4.0.7 on 2023-05-03 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_sitepreferences_maptiler_api_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitepreferences',
            name='default_geometry_checker_params',
            field=models.JSONField(blank=True, default={'gaps_threshold': 0.01, 'overlaps_threshold': 0.01, 'tolerance': 1e-04}),
        ),
    ]
