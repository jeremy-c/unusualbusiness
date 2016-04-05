# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20160405_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='format',
            field=models.CharField(default=b'event', max_length=16, verbose_name='page_format', choices=[(b'event', 'event'), (b'video', 'VIDEO'), (b'text', 'TEXT'), (b'images', 'IMAGES'), ((b'audio',), 'AUDIO'), (b'organization', 'ORGANIZATION'), (b'theory', 'THEORY'), (b'link', 'LINK'), (b'document', 'DOCUMENT')]),
        ),
    ]
