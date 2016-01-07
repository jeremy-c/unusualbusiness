# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('articles', '0001_initial'),
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('tags', '0001_initial'),
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='theoryarticlepage',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='tags.TaggedPage', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='storyarticlepageorganization',
            name='organization_page',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='organizations.OrganizationPage', null=True),
        ),
        migrations.AddField(
            model_name='storyarticlepageorganization',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='organizations', to='articles.StoryArticlePage'),
        ),
        migrations.AddField(
            model_name='storyarticlepage',
            name='featured_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='featured_image', blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AddField(
            model_name='storyarticlepage',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='tags.TaggedPage', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='reportarticlepage',
            name='featured_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='featured_image', blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AddField(
            model_name='reportarticlepage',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='tags.TaggedPage', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
