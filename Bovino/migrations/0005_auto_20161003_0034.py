# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-03 00:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bovino', '0004_auto_20161003_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bovino',
            name='id_madre',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='id_madre_bovino', to='Bovino.Bovino'),
        ),
        migrations.AlterField(
            model_name='bovino',
            name='id_padre',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='id_padre_bovino', to='Bovino.Bovino'),
        ),
    ]