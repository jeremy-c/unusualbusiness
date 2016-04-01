# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20160331_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportarticlepage',
            name='author',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='author', blank=True, to='articles.AuthorPage', null=True),
        ),
        migrations.AddField(
            model_name='storyarticlepage',
            name='author',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='author', blank=True, to='articles.AuthorPage', null=True),
        ),
        migrations.AddField(
            model_name='theoryarticlepage',
            name='author',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='author', blank=True, to='articles.AuthorPage', null=True),
        ),
    ]
