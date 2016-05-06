# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import unusualbusiness.utils.models
import wagtail_modeltranslation.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0028_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefinitionIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_nl', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('slug_en', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_nl', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('url_path_en', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_nl', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('seo_title_en', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_nl', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('search_description_en', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_nl', models.TextField(blank=True, null=True, verbose_name='search description')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_modeltranslation.models.TranslationMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='DefinitionPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_nl', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('slug_en', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_nl', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('url_path_en', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_nl', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('seo_title_en', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_nl', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('search_description_en', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_nl', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('format', models.CharField(choices=[(b'text', 'Normal Article'), (b'theory', 'Theory Article'), (b'video', 'Video embed'), ((b'audio',), 'Audio embed'), (b'images', 'Image slideshow'), (b'event', 'Event'), (b'organization', 'Organization'), (b'link', 'External Link'), (b'document', 'Document Download')], default=b'theory', max_length=32, verbose_name='page_format')),
                ('definition', models.TextField(blank=True, null=True)),
                ('definition_en', models.TextField(blank=True, null=True)),
                ('definition_nl', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_modeltranslation.models.TranslationMixin, 'wagtailcore.page', unusualbusiness.utils.models.RenderInlineMixin),
        ),
    ]
