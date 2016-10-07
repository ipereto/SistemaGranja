# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-06 22:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Municipio', '0002_municipio_id_departamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipio',
            name='id_departamento',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='id_municipio_departamento', to='Departamento.Departamento'),
        ),
    ]