# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_definitionindexpage'),
        ('events', '0005_auto_20160106_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='report_page',
            field=models.ForeignKey(related_name='+', blank=True, to='articles.ReportArticlePage', null=True),
        ),
    ]
