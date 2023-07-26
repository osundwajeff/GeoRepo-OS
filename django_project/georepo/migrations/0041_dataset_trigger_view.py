# Generated by Django 4.0.7 on 2022-12-05 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('georepo', '0040_geographicalentity_simplified_geometry'),
    ]

    operations = [
        migrations.RunSQL(
            'CREATE OR REPLACE FUNCTION filter_refresh_matview()  '
            'RETURNS trigger as $filter_refresh_matview$ '
            'DECLARE '
            'rec RECORD; '
            'BEGIN '
            '    FOR rec IN '
            '        SELECT * '
            '        FROM pg_matviews WHERE ( '
            '            matviewname LIKE \'filter_ds\'|| old.id ||\'_%\') '
            '    loop '
            '        IF TG_OP = \'DELETE\' '
            '        then '
            '          EXECUTE \'DROP MATERIALIZED VIEW IF EXISTS \'|| '
            ' rec.matviewname; '
            '        else '
            '          EXECUTE \'REFRESH MATERIALIZED VIEW CONCURRENTLY \'|| '
            ' rec.matviewname;  '
            '        end if; '
            '    END LOOP;  '
            '    RETURN NULL; '
            'END; '
            '$filter_refresh_matview$ LANGUAGE plpgsql ;'
        ),
        migrations.RunSQL(
            'DROP TRIGGER IF EXISTS '
            'trigger_dataset_filter_refresh on georepo_dataset;'
        ),
        migrations.RunSQL(
            'CREATE TRIGGER trigger_dataset_filter_refresh  '
            'AFTER UPDATE '
            'OR DELETE  '
            'ON georepo_dataset '
            'FOR EACH ROW EXECUTE PROCEDURE filter_refresh_matview();'
        )
    ]
