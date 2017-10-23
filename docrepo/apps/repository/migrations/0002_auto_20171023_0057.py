# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facet',
            name='document',
        ),
        migrations.AddField(
            model_name='facet',
            name='document',
            field=models.ManyToManyField(blank=True, null=True, to='repository.Document'),
        ),
    ]