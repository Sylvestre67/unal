# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 01:40
from __future__ import unicode_literals

import cloudinary.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlickR_Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('photo_feed', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]