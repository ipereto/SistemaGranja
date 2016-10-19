# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-08 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bovino', '0010_auto_20161008_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bovino',
            name='id_madre',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_madre_bovino', to='Bovino.Bovino', verbose_name='Identificaci\xf3n del bovino madre'),
        ),
        migrations.AlterField(
            model_name='bovino',
            name='id_padre',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_padre_bovino', to='Bovino.Bovino', verbose_name='Identificaci\xf3n del bovino padre'),
        ),
        migrations.AlterField(
            model_name='bovino',
            name='id_parto',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='TipoParto.TipoParto', verbose_name='Tipo de parto'),
        ),
        migrations.AlterField(
            model_name='bovino',
            name='peso_nacimiento',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, verbose_name='Peso de nacimiento'),
        ),
    ]
