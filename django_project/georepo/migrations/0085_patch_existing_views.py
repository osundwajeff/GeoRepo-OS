# Generated by Django 4.0.7 on 2023-03-13 04:47
import re
from django.db import migrations
from django.db import connection


def create_sql_view(view):
    view_name = view.uuid
    query_string = view.query_string
    with connection.cursor() as cursor:
        if '*' in query_string and 'join' in query_string.lower():
            # This is join table, get the first table name
            join_tag = 'join'
            if 'left' in query_string.lower():
                join_tag = 'left'
            if 'right' in query_string.lower():
                join_tag = 'right'
            table_name = re.search(
                r'(\w+\s*)' + join_tag, query_string.lower()
            ).group(1).strip()

            column_names_with_table = []
            cursor.execute(
                "SELECT * FROM INFORMATION_SCHEMA.COLUMNS "
                "WHERE TABLE_NAME = N'{view_name}'".format(
                    view_name='georepo_geographicalentity'
                ))
            columns = [col[0] for col in cursor.description]
            col = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            column_names = [c['column_name'] for c in col]
            for column_name in column_names:
                column_names_with_table.append(
                    f'{table_name}.{column_name}'
                )

            query_string = re.sub(
                'select \*',
                'SELECT {}'.format(','.join(column_names_with_table)),
                query_string,
                flags=re.IGNORECASE)
        if view.is_static:
            drop_sql = (
                'DROP MATERIALIZED VIEW IF EXISTS "{view_name}"'
            ).format(
                view_name=view_name
            )
            cursor.execute('''%s''' % drop_sql)
            sql = (
                'CREATE MATERIALIZED VIEW "{view_name}" '
                'AS {sql_raw}'.format(
                    view_name=view_name,
                    sql_raw=query_string
                )
            )
        else:
            sql = (
                'CREATE OR REPLACE VIEW "{view_name}" AS {sql_raw}'.format(
                    view_name=view_name,
                    sql_raw=query_string
                )
            )
        cursor.execute('''%s''' % sql)


def patch_existing_views(apps, schema_editor):
    DatasetView = apps.get_model('georepo', 'DatasetView')
    views = DatasetView.objects.all()
    for view in views:
        create_sql_view(view)


class Migration(migrations.Migration):

    dependencies = [
        ('georepo', '0084_datasetview_max_privacy_level_and_more'),
    ]

    operations = [
        migrations.RunPython(patch_existing_views),
    ]
