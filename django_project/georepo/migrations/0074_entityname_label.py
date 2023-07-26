# Generated by Django 4.0.7 on 2023-03-01 06:25

from django.db import migrations, models


def init_label_entity_name(apps, schema_editor):
    GeographicalEntity = apps.get_model('georepo', 'GeographicalEntity')
    EntityName = apps.get_model('georepo', 'EntityName')
    entity_list = GeographicalEntity.objects.all()
    for entity in entity_list.iterator(chunk_size=1):
        names = EntityName.objects.filter(
            geographical_entity=entity
        ).order_by('id')
        for index, name in enumerate(names):
            name.label = f'Name {index+1}'
            name.save()


class Migration(migrations.Migration):

    dependencies = [
        ('georepo', '0073_dataset_generate_adm0_default_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='entityname',
            name='label',
            field=models.CharField(blank=True, default='', help_text='Examples: Alt Name.', max_length=255, null=True),
        )
    ]
