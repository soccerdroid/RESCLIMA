# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-13 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('layer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RasterLayer',
            fields=[
                ('layer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='layer.Layer')),
                ('file_path', models.CharField(max_length=255)),
                ('file_name', models.CharField(max_length=50)),
                ('file_format', models.CharField(max_length=10)),
                ('projected', models.BooleanField(default=True)),
                ('numBands', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
            bases=('layer.layer',),
        ),
    ]
