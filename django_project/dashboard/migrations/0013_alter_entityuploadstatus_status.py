# Generated by Django 4.0.7 on 2022-10-25 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_remove_layeruploadsession_entities_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entityuploadstatus',
            name='status',
            field=models.CharField(blank=True, choices=[('Started', 'Started'), ('Valid', 'Valid'), ('Error', 'Error'), ('Processing', 'Processing')], default='', max_length=100),
        ),
    ]
