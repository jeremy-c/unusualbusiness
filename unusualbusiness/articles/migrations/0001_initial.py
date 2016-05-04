# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks
import wagtail_modeltranslation.models
import django.db.models.deletion
import wagtail.wagtailimages.blocks
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtailimages', '0010_change_on_delete_behaviour'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorIndexPage',
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
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_modeltranslation.models.TranslationMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='AuthorPage',
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
                ('biography', models.TextField(help_text='The biography of the author (max. 150 woorden)', verbose_name='biography', blank=True)),
                ('biography_en', models.TextField(help_text='The biography of the author (max. 150 woorden)', null=True, verbose_name='biography', blank=True)),
                ('biography_nl', models.TextField(help_text='The biography of the author (max. 150 woorden)', null=True, verbose_name='biography', blank=True)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
            bases=(wagtail_modeltranslation.models.TranslationMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='ReportArticlePage',
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
                ('subtitle', models.CharField(help_text='The subtitle of the page', max_length=255, verbose_name='subtitle', blank=True)),
                ('subtitle_en', models.CharField(help_text='The subtitle of the page', max_length=255, null=True, verbose_name='subtitle', blank=True)),
                ('subtitle_nl', models.CharField(help_text='The subtitle of the page', max_length=255, null=True, verbose_name='subtitle', blank=True)),
                ('format', models.CharField(default=b'text', max_length=32, verbose_name='page_format', choices=[(b'text', 'Normal Article'), (b'theory', 'Theory Article'), (b'video', 'Video embed'), ((b'audio',), 'Audio embed'), (b'images', 'Image slideshow'), (b'event', 'Event'), (b'organization', 'Organization'), (b'link', 'External Link'), (b'document', 'Document Download')])),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now, help_text='The publication date of the article', null=True, verbose_name='publication_date', blank=True)),
                ('body', wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon='italic')), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())])),
                ('body_en', wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon='italic')), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())], null=True)),
                ('body_nl', wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon='italic')), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())], null=True)),
            ],
            options={
                'verbose_name': 'Event report',
            },
            bases=(wagtail_modeltranslation.models.TranslationMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='StoryArticleIndexPage',
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
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_modeltranslation.models.TranslationMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='StoryArticlePage',
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
                ('subtitle', models.CharField(help_text='The subtitle of the page', max_length=255, verbose_name='subtitle', blank=True)),
                ('subtitle_en', models.CharField(help_text='The subtitle of the page', max_length=255, null=True, verbose_name='subtitle', blank=True)),
                ('subtitle_nl', models.CharField(help_text='The subtitle of the page', max_length=255, null=True, verbose_name='subtitle', blank=True)),
                ('format', models.CharField(default=b'text', max_length=32, verbose_name='page_format', choices=[(b'text', 'Normal Article'), (b'theory', 'Theory Article'), (b'video', 'Video embed'), ((b'audio',), 'Audio embed'), (b'images', 'Image slideshow'), (b'event', 'Event'), (b'organization', 'Organization'), (b'link', 'External Link'), (b'document', 'Document Download')])),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now, help_text='The publication date of the article', null=True, verbose_name='publication_date', blank=True)),
                ('body', wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon='italic')), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())])),
                ('body_en', wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon='italic')), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())], null=True)),
                ('body_nl', wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon='italic')), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())], null=True)),
            ],
            options={
                'verbose_name': 'Story',
                'verbose_name_plural': 'Stories',
            },
            bases=(wagtail_modeltranslation.models.TranslationMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='StoryArticlePageOrganization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TheoryArticleIndexPage',
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
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_modeltranslation.models.TranslationMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='TheoryArticlePage',
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
                ('subtitle', models.CharField(help_text='The subtitle of the page', max_length=255, verbose_name='subtitle', blank=True)),
                ('subtitle_en', models.CharField(help_text='The subtitle of the page', max_length=255, null=True, verbose_name='subtitle', blank=True)),
                ('subtitle_nl', models.CharField(help_text='The subtitle of the page', max_length=255, null=True, verbose_name='subtitle', blank=True)),
                ('format', models.CharField(default=b'text', max_length=32, verbose_name='page_format', choices=[(b'text', 'Normal Article'), (b'theory', 'Theory Article'), (b'video', 'Video embed'), ((b'audio',), 'Audio embed'), (b'images', 'Image slideshow'), (b'event', 'Event'), (b'organization', 'Organization'), (b'link', 'External Link'), (b'document', 'Document Download')])),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now, help_text='The publication date of the article', null=True, verbose_name='publication_date', blank=True)),
                ('body', wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon='italic')), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())])),
                ('body_en', wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon='italic')), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())], null=True)),
                ('body_nl', wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.RichTextBlock(icon='italic')), ('chapter', wagtail.wagtailcore.blocks.StructBlock([(b'chapter_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('section', wagtail.wagtailcore.blocks.StructBlock([(b'section_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('subsection', wagtail.wagtailcore.blocks.StructBlock([(b'subsection_name', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('carousel', wagtail.wagtailcore.blocks.StreamBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock())], icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.CharBlock(required=True))])), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock())], null=True)),
                ('author', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='author', blank=True, to='articles.AuthorPage', null=True)),
                ('featured_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='featured_image', blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'verbose_name': 'Theory',
                'verbose_name_plural': 'Theories',
            },
            bases=(wagtail_modeltranslation.models.TranslationMixin, 'wagtailcore.page', models.Model),
        ),
    ]
