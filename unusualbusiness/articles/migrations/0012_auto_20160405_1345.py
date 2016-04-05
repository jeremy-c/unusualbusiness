# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_authorindexpage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authorpage',
            options={'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AddField(
            model_name='reportarticlepage',
            name='format',
            field=models.CharField(max_length=16, null=True, verbose_name='page_format', choices=[(b'event', 'Event'), (b'video', 'Video'), (b'text', 'Text'), (b'images', 'Image slideshow'), (b'audio', 'Audio embed'), (b'organization', 'Organization'), (b'theory', 'Theory'), (b'link', 'External link'), (b'document', 'Document download')]),
        ),
        migrations.AddField(
            model_name='storyarticlepage',
            name='format',
            field=models.CharField(max_length=16, null=True, verbose_name='page_format', choices=[(b'event', 'Event'), (b'video', 'Video'), (b'text', 'Text'), (b'images', 'Image slideshow'), (b'audio', 'Audio embed'), (b'organization', 'Organization'), (b'theory', 'Theory'), (b'link', 'External link'), (b'document', 'Document download')]),
        ),
        migrations.AddField(
            model_name='theoryarticlepage',
            name='format',
            field=models.CharField(max_length=16, null=True, verbose_name='page_format', choices=[(b'event', 'Event'), (b'video', 'Video'), (b'text', 'Text'), (b'images', 'Image slideshow'), (b'audio', 'Audio embed'), (b'organization', 'Organization'), (b'theory', 'Theory'), (b'link', 'External link'), (b'document', 'Document download')]),
        ),
    ]
