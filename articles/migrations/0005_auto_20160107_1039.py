# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('articles', '0004_auto_20160106_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='definitionindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='definitionpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='DefinitionIndexPage',
        ),
        migrations.DeleteModel(
            name='DefinitionPage',
        ),
    ]
