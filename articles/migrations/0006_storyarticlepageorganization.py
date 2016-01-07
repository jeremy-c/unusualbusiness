# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_auto_20160107_1039'),
        ('articles', '0005_auto_20160107_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryArticlePageOrganization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('organization_page', models.ForeignKey(to='organizations.OrganizationPage')),
                ('story_article_page', modelcluster.fields.ParentalKey(related_name='organizations', to='articles.StoryArticlePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
