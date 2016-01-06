# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_eventpage_report_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='report_page',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='articles.ReportArticlePage', null=True),
        ),
    ]
