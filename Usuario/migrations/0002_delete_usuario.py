# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-06 05:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]