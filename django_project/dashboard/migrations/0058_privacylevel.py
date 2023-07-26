# Generated by Django 4.0.7 on 2023-07-12 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0057_add_simplify_function'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privacy_level', models.PositiveIntegerField(unique=True)),
                ('label', models.CharField(max_length=30)),
            ],
        ),
        migrations.RunSQL(
            """INSERT INTO public.dashboard_privacylevel (privacy_level, "label") VALUES(1, 'Publicly shareable');""",
            reverse_sql="""DELETE FROM public.dashboard_privacylevel WHERE privacy_level=1"""
        ),
        migrations.RunSQL(
            """INSERT INTO public.dashboard_privacylevel (privacy_level, "label") VALUES(2, 'Low confidential');""",
            reverse_sql="""DELETE FROM public.dashboard_privacylevel WHERE privacy_level=2"""
        ),
        migrations.RunSQL(
            """INSERT INTO public.dashboard_privacylevel (privacy_level, "label") VALUES(3, 'Medium confidential');""",
            reverse_sql="""DELETE FROM public.dashboard_privacylevel WHERE privacy_level=3"""
        ),
        migrations.RunSQL(
            """INSERT INTO public.dashboard_privacylevel (privacy_level, "label") VALUES(4, 'Highly confidential');""",
            reverse_sql="""DELETE FROM public.dashboard_privacylevel WHERE privacy_level=4"""
        )
    ]
