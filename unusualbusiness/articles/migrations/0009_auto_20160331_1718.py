# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_authorpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportarticlepage',
            name='author',
        ),
        migrations.RemoveField(
            model_name='storyarticlepage',
            name='author',
        ),
        migrations.RemoveField(
            model_name='theoryarticlepage',
            name='author',
        ),
    ]
