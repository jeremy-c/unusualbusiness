# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_storyarticlepageorganization'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storyarticlepageorganization',
            old_name='story_article_page',
            new_name='page',
        ),
    ]
