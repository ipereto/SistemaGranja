# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-05 19:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Municipio', '0001_initial'),
        ('Granja', '0004_granja_zona_vida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='granja',
            name='municipio',
        ),
        migrations.AddField(
            model_name='granja',
            name='id_municipio',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='id_granja_municipio', to='Municipio.Municipio'),
        ),
        migrations.AlterField(
            model_name='granja',
            name='id_departamento',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='id_granja_departamento', to='Departamento.Departamento'),
        ),
        migrations.AlterField(
            model_name='granja',
            name='id_granja',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
