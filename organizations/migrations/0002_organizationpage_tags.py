# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('tags', '0001_initial'),
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationpage',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='tags.TaggedPage', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
