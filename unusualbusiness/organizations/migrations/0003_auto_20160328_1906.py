# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_organizationpage_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationpage',
            name='description',
            field=models.CharField(default='', max_length=512, verbose_name='Description', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organizationpage',
            name='description_en',
            field=models.CharField(max_length=512, null=True, verbose_name='Description', blank=True),
        ),
        migrations.AlterField(
            model_name='organizationpage',
            name='description_nl',
            field=models.CharField(max_length=512, null=True, verbose_name='Description', blank=True),
        ),
    ]
