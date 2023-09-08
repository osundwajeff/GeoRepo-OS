# Generated by Django 4.0.7 on 2023-09-07 18:07

from django.db import migrations


def init_default_template(apps, schema_editor):
    SitePreferences = apps.get_model('core', 'SitePreferences')
    preferences, _ = SitePreferences.objects.get_or_create(pk=1)
    preferences.tile_configs_template = [
        {
            "zoom_level": 0,
            "tile_configs": [
                {
                    "level": "0",
                    "tolerance": 1
                }
            ]
        },
        {
            "zoom_level": 1,
            "tile_configs": [
                {
                    "level": "0",
                    "tolerance": 1
                },
                {
                    "level": "1",
                    "tolerance": 1
                }
            ]
        },
        {
            "zoom_level": 2,
            "tile_configs": [
                {
                    "level": "0",
                    "tolerance": 1
                },
                {
                    "level": "1",
                    "tolerance": 1
                }
            ]
        },
        {
            "zoom_level": 3,
            "tile_configs": [
                {
                    "level": "0",
                    "tolerance": 1
                },
                {
                    "level": "1",
                    "tolerance": 1
                },
                {
                    "level": "2",
                    "tolerance": 1
                }
            ]
        },
        {
            "zoom_level": 4,
            "tile_configs": [
                {
                    "level": "0",
                    "tolerance": 1
                },
                {
                    "level": "1",
                    "tolerance": 1
                },
                {
                    "level": "2",
                    "tolerance": 1
                },
                {
                    "level": "3",
                    "tolerance": 1
                }
            ]
        },
        {
            "zoom_level": 5,
            "tile_configs": [
                {
                    "level": "0",
                    "tolerance": 1
                },
                {
                    "level": "1",
                    "tolerance": 1
                },
                {
                    "level": "2",
                    "tolerance": 1
                },
                {
                    "level": "3",
                    "tolerance": 1
                },
                {
                    "level": "4",
                    "tolerance": 1
                }
            ]
        },
        {
            "zoom_level": 6,
            "tile_configs": [
                {
                    "level": "0",
                    "tolerance": 1
                },
                {
                    "level": "1",
                    "tolerance": 1
                },
                {
                    "level": "2",
                    "tolerance": 1
                },
                {
                    "level": "3",
                    "tolerance": 1
                },
                {
                    "level": "4",
                    "tolerance": 1
                },
                {
                    "level": "5",
                    "tolerance": 1
                }
            ]
        },
        {
            "zoom_level": 7,
            "tile_configs": [
                {
                    "level": "0",
                    "tolerance": 1
                },
                {
                    "level": "1",
                    "tolerance": 1
                },
                {
                    "level": "2",
                    "tolerance": 1
                },
                {
                    "level": "3",
                    "tolerance": 1
                },
                {
                    "level": "4",
                    "tolerance": 1
                },
                {
                    "level": "5",
                    "tolerance": 1
                },
                {
                    "level": "6",
                    "tolerance": 1
                }
            ]
        },
        {
            "zoom_level": 8,
            "tile_configs": [
                {
                    "level": "0",
                    "tolerance": 1
                },
                {
                    "level": "1",
                    "tolerance": 1
                },
                {
                    "level": "2",
                    "tolerance": 1
                },
                {
                    "level": "3",
                    "tolerance": 1
                },
                {
                    "level": "4",
                    "tolerance": 1
                },
                {
                    "level": "5",
                    "tolerance": 1
                },
                {
                    "level": "6",
                    "tolerance": 1
                }
            ]
        }
    ]
    preferences.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_delete_old_keys'),
    ]

    operations = [
        migrations.RunPython(init_default_template),
    ]
