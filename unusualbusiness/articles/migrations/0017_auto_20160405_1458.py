# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_auto_20160405_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportarticlepage',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 5, 12, 58, 13, 142654, tzinfo=utc), auto_now_add=True, help_text='The publication date of the article', verbose_name='publication_date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='storyarticlepage',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 5, 12, 58, 18, 110318, tzinfo=utc), auto_now_add=True, help_text='The publication date of the article', verbose_name='publication_date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='theoryarticlepage',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 5, 12, 58, 19, 966517, tzinfo=utc), auto_now_add=True, help_text='The publication date of the article', verbose_name='publication_date'),
            preserve_default=False,
        ),
    ]
