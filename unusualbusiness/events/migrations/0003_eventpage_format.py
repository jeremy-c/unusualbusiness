# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_eventpage_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='format',
            field=models.CharField(max_length=16, null=True, verbose_name='page_format', choices=[(b'event', 'Event')]),
        ),
    ]
