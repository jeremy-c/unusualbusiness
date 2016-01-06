# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail_modeltranslation.models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtailimages', '0010_change_on_delete_behaviour'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_modeltranslation.models.TranslationMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('start_date', models.DateField(null=True, verbose_name='Starting date')),
                ('start_time', models.TimeField(verbose_name='Starting time')),
                ('end_date', models.DateField(null=True, verbose_name='End date')),
                ('end_time', models.TimeField(verbose_name='End time')),
                ('location', models.CharField(max_length=512, verbose_name='Location', blank=True)),
                ('description', wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Description')),
                ('poster_link', models.URLField(verbose_name='Poster', blank=True)),
                ('flyer_link', models.URLField(verbose_name='Flyer', blank=True)),
                ('facebook_event', models.URLField(verbose_name='Facebook event', blank=True)),
                ('featured_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Featured image', blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_modeltranslation.models.TranslationMixin, 'wagtailcore.page'),
        ),
    ]
