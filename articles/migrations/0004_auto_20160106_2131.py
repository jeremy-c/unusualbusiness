# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_definitionindexpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='definitionindexpage',
            name='search_description_en',
            field=models.TextField(null=True, verbose_name='search description', blank=True),
        ),
        migrations.AddField(
            model_name='definitionindexpage',
            name='search_description_nl',
            field=models.TextField(null=True, verbose_name='search description', blank=True),
        ),
        migrations.AddField(
            model_name='definitionindexpage',
            name='seo_title_en',
            field=models.CharField(help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title', blank=True),
        ),
        migrations.AddField(
            model_name='definitionindexpage',
            name='seo_title_nl',
            field=models.CharField(help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title', blank=True),
        ),
        migrations.AddField(
            model_name='definitionindexpage',
            name='slug_en',
            field=models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='definitionindexpage',
            name='slug_nl',
            field=models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='definitionindexpage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='definitionindexpage',
            name='title_nl',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='definitionindexpage',
            name='url_path_en',
            field=models.TextField(verbose_name='URL path', null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='definitionindexpage',
            name='url_path_nl',
            field=models.TextField(verbose_name='URL path', null=True, editable=False, blank=True),
        ),
    ]
