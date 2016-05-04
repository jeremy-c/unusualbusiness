# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('howtos', '0001_initial'),
        ('events', '0001_initial'),
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='howtopageorganizationpage',
            name='organization',
            field=models.ForeignKey(related_name='how_to_page', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='organizations.OrganizationPage', null=True),
        ),
        migrations.AddField(
            model_name='howtopageeventpage',
            name='event',
            field=models.ForeignKey(related_name='how_to_page', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='events.EventPage', null=True),
        ),
        migrations.AddField(
            model_name='howtopageeventpage',
            name='how_to_page',
            field=modelcluster.fields.ParentalKey(related_name='event_pages', to='howtos.HowToPage'),
        ),
        migrations.AddField(
            model_name='howtopage',
            name='featured_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Featured image', blank=True, to='wagtailimages.Image', null=True),
        ),
    ]
