# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howtos', '0002_howtopage_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='howtoindexpage',
            options={'verbose_name': 'How to Index Page', 'verbose_name_plural': 'How to Index Pages'},
        ),
        migrations.AlterModelOptions(
            name='howtopage',
            options={'verbose_name': 'How to', 'verbose_name_plural': "How to's"},
        ),
    ]
