# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import django.db.models.deletion
import wagtail_modeltranslation.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtailimages', '0010_change_on_delete_behaviour'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_nl', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('slug_en', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_nl', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('url_path_en', models.TextField(verbose_name='URL path', null=True, editable=False, blank=True)),
                ('url_path_nl', models.TextField(verbose_name='URL path', null=True, editable=False, blank=True)),
                ('seo_title_en', models.CharField(help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title', blank=True)),
                ('seo_title_nl', models.CharField(help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title', blank=True)),
                ('search_description_en', models.TextField(null=True, verbose_name='search description', blank=True)),
                ('search_description_nl', models.TextField(null=True, verbose_name='search description', blank=True)),
                ('description', wagtail.wagtailcore.fields.RichTextField()),
                ('description_en', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('description_nl', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('date_founded', models.DateField(verbose_name='Founded date')),
                ('feed_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_modeltranslation.models.TranslationMixin, 'wagtailcore.page'),
        ),
    ]
