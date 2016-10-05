# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-03 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id_medicamento', models.AutoField(primary_key=True, serialize=False)),
                ('producto', models.CharField(max_length=140)),
                ('laboratorio', models.CharField(max_length=140)),
                ('reg_ica', models.CharField(max_length=140)),
                ('numeroLote', models.CharField(max_length=140)),
                ('observacion', models.CharField(max_length=140)),
                ('fechaVencimiento', models.DateTimeField()),
            ],
            options={
                'ordering': ('id_medicamento',),
            },
        ),
    ]