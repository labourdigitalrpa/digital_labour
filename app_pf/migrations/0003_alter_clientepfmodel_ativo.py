# Generated by Django 3.2.13 on 2022-05-05 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pf', '0002_rename_cliente_pf_clientepfmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientepfmodel',
            name='ativo',
            field=models.BooleanField(),
        ),
    ]
