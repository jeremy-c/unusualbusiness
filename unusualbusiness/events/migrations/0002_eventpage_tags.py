# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 09:47
from __future__ import unicode_literals

from django.db import migrations
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('events', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='tags.EventPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
