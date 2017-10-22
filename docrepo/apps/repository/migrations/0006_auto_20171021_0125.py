# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 01:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_documentversion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depiction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('content_file', models.FileField(upload_to='content/%Y/%m/%d/%H/%M')),
                ('file_type', models.CharField(choices=[('image', 'image'), ('pdf', 'pdf')], max_length=30, verbose_name='File Type')),
            ],
            options={
                'verbose_name': 'Depiction',
                'verbose_name_plural': 'Depictions',
            },
        ),
        migrations.AlterModelOptions(
            name='documentversion',
            options={'verbose_name': 'Document Version', 'verbose_name_plural': 'Document Versions'},
        ),
        migrations.AlterField(
            model_name='documentversion',
            name='content_file',
            field=models.FileField(upload_to='content/%Y/%m/%d/%H/%M'),
        ),
        migrations.AddField(
            model_name='depiction',
            name='document_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.DocumentVersion'),
        ),
    ]
