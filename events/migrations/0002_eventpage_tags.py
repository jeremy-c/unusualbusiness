# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('events', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(to='taggit.Tag', through='tags.EventPageTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
