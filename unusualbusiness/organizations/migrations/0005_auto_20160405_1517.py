# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_organizationpage_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationpage',
            name='format',
            field=models.CharField(default=((b'organization', 'Organization'),), max_length=16, verbose_name='page_format', choices=[(b'organization', 'Organization')]),
        ),
    ]
