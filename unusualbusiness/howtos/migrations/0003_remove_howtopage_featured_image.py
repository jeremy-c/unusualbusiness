# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 13:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('howtos', '0002_auto_20160907_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='howtopage',
            name='featured_image',
        ),
    ]