# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20160405_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='format',
            field=models.CharField(default=b'event', max_length=16, verbose_name='page_format', choices=[(b'text', 'Normal Article'), (b'theory', 'Theory Article'), (b'video', 'Video embed'), ((b'audio',), 'Audio embed'), (b'images', 'Image slideshow'), (b'event', 'Event'), (b'organization', 'Organization'), (b'link', 'External Link'), (b'document', 'Document Download')]),
        ),
    ]
