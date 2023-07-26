# Generated by Django 3.2.16 on 2023-04-13 04:41

import django.db.models.deletion
from django.db import migrations, models

from azure_auth.models import RegisteredDomain


def default_domain(apps, schema_editor):
    """Create default domain."""
    RegisteredDomain.objects.get_or_create(domain='unicef.org')


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredDomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=256, unique=True)),
                ('group', models.ForeignKey(blank=True, help_text='Autoassign user under the domain to the group.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group')),
            ],
        ),
        migrations.RunPython(default_domain, migrations.RunPython.noop),
    ]
