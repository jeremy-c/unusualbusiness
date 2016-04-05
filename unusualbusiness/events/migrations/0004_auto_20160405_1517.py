# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_eventpage_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='format',
            field=models.CharField(default=((b'event', 'Event'),), max_length=16, verbose_name='page_format', choices=[(b'event', 'Event')]),
        ),
    ]
