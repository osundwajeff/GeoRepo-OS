# Generated by Django 4.0.7 on 2023-03-07 09:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('georepo', '0076_merge_0075_entityname_idx_0075_update_view_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatasetViewResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privacy_level', models.IntegerField(default=4)),
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='UUID')),
                ('status', models.CharField(choices=[('PE', 'Pending'), ('PR', 'Processing'), ('DO', 'Done'), ('ER', 'Error')], default='PE', max_length=2)),
                ('vector_tiles_task_id', models.CharField(blank=True, default='', max_length=256)),
                ('vector_tiles_updated_at', models.DateTimeField(auto_now_add=True)),
                ('vector_tiles_progress', models.FloatField(blank=True, default=0, null=True)),
                ('vector_tiles_log', models.TextField(blank=True, default='')),
                ('dataset_view', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='georepo.datasetview')),
            ],
        ),
        migrations.AddConstraint(
            model_name='datasetviewresource',
            constraint=models.UniqueConstraint(fields=('dataset_view', 'privacy_level'), name='unique_view_resource'),
        ),
    ]
