# Generated by Django 4.0.7 on 2023-03-09 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('georepo', '0080_alter_dataset_options_alter_module_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='max_privacy_level',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='dataset',
            name='min_privacy_level',
            field=models.IntegerField(default=1),
        ),
    ]
