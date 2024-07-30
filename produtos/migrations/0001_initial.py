# Generated by Django 5.0.2 on 2024-07-30 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('preco_unit', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]