# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import datetime
import wagtail.wagtailcore.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('events', '0004_eventpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='description_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='description_nl',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='end_date',
            field=models.DateTimeField(null=True, verbose_name='End date'),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='facebook_event',
            field=models.URLField(verbose_name='Facebook event', blank=True),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='featured_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Featured image', blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='flyer_link',
            field=models.URLField(verbose_name='Flyer', blank=True),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='location',
            field=models.CharField(max_length=512, verbose_name='Location', blank=True),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='poster_link',
            field=models.URLField(verbose_name='Poster', blank=True),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 11, 52, 46, 847738, tzinfo=utc), verbose_name='Starting date'),
            preserve_default=False,
        ),
    ]
