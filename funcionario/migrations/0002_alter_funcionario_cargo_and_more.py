# Generated by Django 5.0.2 on 2024-07-10 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cargo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='data_admissao',
            field=models.DateField(blank=True, null=True),
        ),
    ]
