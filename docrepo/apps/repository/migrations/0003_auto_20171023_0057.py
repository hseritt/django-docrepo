# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0002_auto_20171023_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facet',
            name='document',
            field=models.ManyToManyField(to='repository.Document'),
        ),
    ]
