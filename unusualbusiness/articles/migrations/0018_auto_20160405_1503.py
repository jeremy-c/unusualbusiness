# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_auto_20160405_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportarticlepage',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 5, 13, 3, 0, 335770, tzinfo=utc), help_text='The publication date of the article', verbose_name='publication_date'),
        ),
        migrations.AlterField(
            model_name='storyarticlepage',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 5, 13, 3, 0, 335770, tzinfo=utc), help_text='The publication date of the article', verbose_name='publication_date'),
        ),
        migrations.AlterField(
            model_name='theoryarticlepage',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 5, 13, 3, 0, 335770, tzinfo=utc), help_text='The publication date of the article', verbose_name='publication_date'),
        ),
    ]
