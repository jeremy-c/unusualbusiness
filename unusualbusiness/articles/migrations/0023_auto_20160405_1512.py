# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0022_auto_20160405_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportarticlepage',
            name='publication_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='The publication date of the article', null=True, verbose_name='publication_date', blank=True),
        ),
        migrations.AlterField(
            model_name='storyarticlepage',
            name='publication_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='The publication date of the article', null=True, verbose_name='publication_date', blank=True),
        ),
        migrations.AlterField(
            model_name='theoryarticlepage',
            name='publication_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='The publication date of the article', null=True, verbose_name='publication_date', blank=True),
        ),
    ]
