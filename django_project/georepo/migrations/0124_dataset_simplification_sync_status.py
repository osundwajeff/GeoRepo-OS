# Generated by Django 4.0.7 on 2023-10-04 15:52

from django.db import migrations, models


def patch_simplification_status(apps, schema_editor):
    Dataset = apps.get_model('georepo', 'Dataset')
    datasets = Dataset.objects.filter(is_simplified=True)
    datasets.update(
        simplification_sync_status='synced'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('georepo', '0123_viewadminleveltilingconfig_georepo_vie_view_ti_9b07a3_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='simplification_sync_status',
            field=models.CharField(choices=[('out_of_sync', 'Out of Sync'), ('syncing', 'Syncing'), ('synced', 'Synced')], default='out_of_sync', max_length=15),
        ),
        migrations.RunPython(patch_simplification_status),
    ]
