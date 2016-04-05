# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20160405_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportarticlepage',
            name='publication_date',
            field=models.DateField(auto_now_add=True, help_text='The publication date of the article', null=True, verbose_name='publication_date'),
        ),
        migrations.AlterField(
            model_name='storyarticlepage',
            name='publication_date',
            field=models.DateField(auto_now_add=True, help_text='The publication date of the article', null=True, verbose_name='publication_date'),
        ),
        migrations.AlterField(
            model_name='theoryarticlepage',
            name='publication_date',
            field=models.DateField(auto_now_add=True, help_text='The publication date of the article', null=True, verbose_name='publication_date'),
        ),
    ]
