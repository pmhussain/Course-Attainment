# Generated by Django 4.2.7 on 2024-02-28 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0004_po_pso_rename_course_outcome_co_co_po_mapping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pso',
            old_name='po',
            new_name='pso',
        ),
    ]
