# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('organizations', '0003_auto_20151222_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationpage',
            name='feed_image',
        ),
        migrations.AddField(
            model_name='organizationpage',
            name='amount_of_members',
            field=models.PositiveIntegerField(null=True, verbose_name='Amount of members'),
        ),
        migrations.AddField(
            model_name='organizationpage',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email', blank=True),
        ),
        migrations.AddField(
            model_name='organizationpage',
            name='facebook',
            field=models.URLField(verbose_name='Facebook', blank=True),
        ),
        migrations.AddField(
            model_name='organizationpage',
            name='featured_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Featured image', blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AddField(
            model_name='organizationpage',
            name='location',
            field=models.CharField(max_length=512, verbose_name='Location', blank=True),
        ),
        migrations.AddField(
            model_name='organizationpage',
            name='website',
            field=models.URLField(verbose_name='Website', blank=True),
        ),
        migrations.AlterField(
            model_name='organizationpage',
            name='date_founded',
            field=models.DateField(null=True, verbose_name='Founded date'),
        ),
        migrations.AlterField(
            model_name='organizationpage',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='organizationpage',
            name='description_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='organizationpage',
            name='description_nl',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Description'),
        ),
    ]
