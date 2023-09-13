# Generated by Django 4.0.7 on 2023-09-13 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_sitepreferences_swagger_ui_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitepreferences',
            name='swagger_ui_info',
            field=models.TextField(default='', help_text='Readme URL shown at the top of Swagger UI.'),
        ),
    ]
