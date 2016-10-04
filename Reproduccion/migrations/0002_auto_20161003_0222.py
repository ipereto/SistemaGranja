# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-03 02:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SemenToro', '0001_initial'),
        ('Bovino', '0005_auto_20161003_0034'),
        ('Servicio', '0001_initial'),
        ('Reproduccion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reproduccion',
            name='id_semen_toro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_reproduccion_semen', to='SemenToro.SemenToro'),
        ),
        migrations.AddField(
            model_name='reproduccion',
            name='id_servicio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='id_reproduccion_servicio', to='Servicio.Servicio'),
        ),
        migrations.AddField(
            model_name='reproduccion',
            name='id_toro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_reproduccion_toro', to='Bovino.Bovino'),
        ),
    ]
