# Generated by Django 4.0.7 on 2023-08-22 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_sitepreferences_api_config_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customapikey',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
