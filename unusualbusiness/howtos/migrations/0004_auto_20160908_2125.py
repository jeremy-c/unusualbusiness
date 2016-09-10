# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-08 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howtos', '0003_remove_howtopage_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='howtoindexpage',
            name='slug_en',
            field=models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='howtoindexpage',
            name='slug_nl',
            field=models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='howtopage',
            name='slug_en',
            field=models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='howtopage',
            name='slug_nl',
            field=models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug'),
        ),
    ]