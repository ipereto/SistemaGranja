# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-05 19:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Departamento', '0002_auto_20161003_0021'),
        ('Municipio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipio',
            name='id_departamento',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='id_municipio_departamento', to='Departamento.Departamento'),
        ),
    ]
