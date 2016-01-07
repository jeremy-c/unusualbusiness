# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20160106_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='end_date',
            field=models.DateTimeField(null=True, verbose_name='End date', blank=True),
        ),
    ]
