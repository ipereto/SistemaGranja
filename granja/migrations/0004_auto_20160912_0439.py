# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-12 04:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('granja', '0003_granja_mapa'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='granja',
            options={'ordering': ('id',)},
        ),
    ]
