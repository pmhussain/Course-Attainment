# Generated by Django 4.2.7 on 2024-03-02 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0025_rename_question_external_question_intenal_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_attainment',
            name='direct',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='course_attainment',
            name='external',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='course_attainment',
            name='internal',
            field=models.FloatField(default=0, null=True),
        ),
    ]