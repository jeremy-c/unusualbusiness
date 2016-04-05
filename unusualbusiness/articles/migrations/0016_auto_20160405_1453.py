# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_auto_20160405_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportarticlepage',
            name='publication_date',
            field=models.DateField(help_text='The publication date of the article', null=True, verbose_name='publication_date', blank=True),
        ),
        migrations.AlterField(
            model_name='storyarticlepage',
            name='publication_date',
            field=models.DateField(help_text='The publication date of the article', null=True, verbose_name='publication_date', blank=True),
        ),
        migrations.AlterField(
            model_name='theoryarticlepage',
            name='publication_date',
            field=models.DateField(help_text='The publication date of the article', null=True, verbose_name='publication_date', blank=True),
        ),
    ]
