# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_auto_20160105_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationpage',
            name='date_founded',
            field=models.DateField(null=True, verbose_name='Founded date', blank=True),
        ),
    ]
