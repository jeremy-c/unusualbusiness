# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('definitions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='definitionpage',
            name='format',
            field=models.CharField(default='text', max_length=16, verbose_name='page_format', choices=[(b'theory', 'Theory')]),
            preserve_default=False,
        ),
    ]
