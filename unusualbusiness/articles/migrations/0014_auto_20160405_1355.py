# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_auto_20160405_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportarticlepage',
            name='publication_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 5, 11, 55, 10, 146767, tzinfo=utc), auto_now_add=True, help_text='The publication date of the article', verbose_name='publication_date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='storyarticlepage',
            name='publication_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 5, 11, 55, 14, 514686, tzinfo=utc), auto_now_add=True, help_text='The publication date of the article', verbose_name='publication_date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='theoryarticlepage',
            name='publication_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 5, 11, 55, 16, 450386, tzinfo=utc), auto_now_add=True, help_text='The publication date of the article', verbose_name='publication_date'),
            preserve_default=False,
        ),
    ]
