# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-08 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('layer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.CharField(max_length=255)),
                ('file_name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=10)),
                ('layers', models.ManyToManyField(to='layer.Layer')),
            ],
        ),
    ]