# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-02 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bovino',
            fields=[
                ('id_bovino', models.CharField(max_length=140, primary_key=True, serialize=False)),
            ],
        ),
    ]
