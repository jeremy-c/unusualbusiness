# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20160107_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyarticlepageorganization',
            name='organization_page',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='organizations.OrganizationPage', null=True),
        ),
    ]
