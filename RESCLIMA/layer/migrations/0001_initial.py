# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-08 21:55
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts_index', django.contrib.postgres.search.SearchVectorField(null=True)),
                ('title', models.CharField(max_length=50, null=True)),
                ('abstract', models.TextField(max_length=500, null=True)),
                ('type', models.CharField(max_length=10)),
                ('data_date', models.DateField(blank=True, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('srs_wkt', models.TextField(max_length=500)),
                ('bbox', django.contrib.gis.db.models.fields.PolygonField(null=True, srid=4326)),
                ('categories', models.ManyToManyField(blank=True, to='search.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
