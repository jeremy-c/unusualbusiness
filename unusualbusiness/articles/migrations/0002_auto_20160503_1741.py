# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.contrib.taggit
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('tags', '0001_initial'),
        ('taggit', '0002_auto_20150616_2121'),
        ('organizations', '0001_initial'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='theoryarticlepage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(to='taggit.Tag', through='tags.TheoryArticlePageTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='storyarticlepageorganization',
            name='organization_page',
            field=models.ForeignKey(related_name='story_article_page', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='organizations.OrganizationPage', null=True),
        ),
        migrations.AddField(
            model_name='storyarticlepageorganization',
            name='story_article_page',
            field=modelcluster.fields.ParentalKey(related_name='organizations', to='articles.StoryArticlePage'),
        ),
        migrations.AddField(
            model_name='storyarticlepage',
            name='author',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='author', blank=True, to='articles.AuthorPage', null=True),
        ),
        migrations.AddField(
            model_name='storyarticlepage',
            name='featured_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='featured_image', blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AddField(
            model_name='storyarticlepage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(to='taggit.Tag', through='tags.StoryArticlePageTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='reportarticlepage',
            name='author',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='author', blank=True, to='articles.AuthorPage', null=True),
        ),
        migrations.AddField(
            model_name='reportarticlepage',
            name='event_page',
            field=models.ForeignKey(related_name='report_article_page', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='events.EventPage', null=True),
        ),
        migrations.AddField(
            model_name='reportarticlepage',
            name='featured_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='featured_image', blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AddField(
            model_name='reportarticlepage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(to='taggit.Tag', through='tags.ReportArticlePageTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='authorpage',
            name='photo',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='photo', blank=True, to='wagtailimages.Image', null=True),
        ),
    ]
