# Generated by Django 4.0.7 on 2023-01-10 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('georepo', '0047_delete_entitytypetilingconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entityid',
            name='geographical_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_ids', to='georepo.geographicalentity'),
        ),
    ]
