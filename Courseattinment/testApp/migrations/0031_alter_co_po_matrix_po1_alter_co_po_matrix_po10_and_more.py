# Generated by Django 4.2.7 on 2024-03-03 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0030_delete_cot_porpso_matrix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='co_po_matrix',
            name='po1',
            field=models.CharField(choices=[('-', 0), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='co_po_matrix',
            name='po10',
            field=models.CharField(choices=[('-', 0), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='co_po_matrix',
            name='po11',
            field=models.CharField(choices=[('-', 0), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='co_po_matrix',
            name='po12',
            field=models.CharField(choices=[('-', 0), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='co_po_matrix',
            name='po2',
            field=models.CharField(choices=[('-', 0), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='co_po_matrix',
            name='po3',
            field=models.CharField(choices=[('-', 0), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='co_po_matrix',
            name='po4',
            field=models.CharField(choices=[('-', 0), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='co_po_matrix',
            name='po5',
            field=models.CharField(choices=[('-', 0), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='co_po_matrix',
            name='po6',
            field=models.CharField(choices=[('-', 0), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='co_po_matrix',
            name='po7',
            field=models.CharField(choices=[('-', 0), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='co_po_matrix',
            name='po8',
            field=models.CharField(choices=[('-', 0), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='co_po_matrix',
            name='po9',
            field=models.CharField(choices=[('-', 0), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='co_po_matrix',
            name='pso1',
            field=models.CharField(choices=[('-', 0), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='co_po_matrix',
            name='pso2',
            field=models.CharField(choices=[('-', 0), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='co_po_matrix',
            name='pso3',
            field=models.CharField(choices=[('-', 0), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10),
        ),
        migrations.CreateModel(
            name='PSO_Attainment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attainment', models.FloatField(default=0, null=True)),
                ('pso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.pso')),
            ],
        ),
    ]
