# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-03 02:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Granja', '0002_granja_id_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='granja',
            name='zona_vida',
        ),
    ]
