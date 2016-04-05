# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_auto_20160328_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationpage',
            name='format',
            field=models.CharField(max_length=16, null=True, verbose_name='page_format', choices=[(b'organization', 'Organization')]),
        ),
    ]
