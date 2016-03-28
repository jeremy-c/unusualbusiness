# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.db import models, migrations
from wagtail.wagtailcore.rich_text import RichText


# # StoryArticlePage
# def convert_to_streamfield_story_article_page(apps, schema_editor):
#     StoryArticlePage = apps.get_model('articles.StoryArticlePage')
#     for page in StoryArticlePage.objects.all():
#         if page.body.raw_text and not page.body:
#             page.body = [('paragraph', RichText(page.body.raw_text))]
#         if page.body_en.raw_text and not page.body_en:
#             page.body_en = [('paragraph', RichText(page.body_en.raw_text))]
#         if page.body_nl.raw_text and not page.body_nl:
#             page.body_nl = [('paragraph', RichText(page.body_nl.raw_text))]
#         page.save()
#
#
# def convert_to_richtext_story_article_page(apps, schema_editor):
#     StoryArticlePage = apps.get_model('articles.StoryArticlePage')
#
#     for page in StoryArticlePage.objects.all():
#         if page.body.raw_text is None:
#             raw_text = ''.join([
#                 child.value.source for child in page.body if child.block_type == 'paragraph'
#             ])
#             page.body = raw_text
#         if page.body_en.raw_text is None:
#             raw_text = ''.join([
#                child.value.source for child in page.body_en if child.block_type == 'paragraph'
#             ])
#             page.body_en = raw_text
#         if page.body_nl.raw_text is None:
#             raw_text = ''.join([
#                child.value.source for child in page.body_nl if child.block_type == 'paragraph'
#             ])
#             page.body_nl = raw_text
#         page.save()
#
#
# # ReportArticlePage
# def convert_to_streamfield_report_article_page(apps, schema_editor):
#     ReportArticlePage = apps.get_model('articles.ReportArticlePage')
#     for page in ReportArticlePage.objects.all():
#         if page.body.raw_text and not page.body:
#             page.body = [('paragraph', RichText(page.body.raw_text))]
#         if page.body_en.raw_text and not page.body_en:
#             page.body_en = [('paragraph', RichText(page.body_en.raw_text))]
#         if page.body_nl.raw_text and not page.body_nl:
#             page.body_nl = [('paragraph', RichText(page.body_nl.raw_text))]
#         page.save()
#
#
# def convert_to_richtext_report_article_page(apps, schema_editor):
#     ReportArticlePage = apps.get_model('articles.ReportArticlePage')
#
#     for page in ReportArticlePage.objects.all():
#         if page.body.raw_text is None:
#             raw_text = ''.join([
#                 child.value.source for child in page.body if child.block_type == 'paragraph'
#             ])
#             page.body = raw_text
#         if page.body_en.raw_text is None:
#             raw_text = ''.join([
#                child.value.source for child in page.body_en if child.block_type == 'paragraph'
#             ])
#             page.body_en = raw_text
#         if page.body_nl.raw_text is None:
#             raw_text = ''.join([
#                child.value.source for child in page.body_nl if child.block_type == 'paragraph'
#             ])
#             page.body_nl = raw_text
#         page.save()
#
#
# # TheoryArticlePage
# def convert_to_streamfield_theory_article_page(apps, schema_editor):
#     TheoryArticlePage = apps.get_model('articles.TheoryArticlePage')
#
#     for page in TheoryArticlePage.objects.all():
#         if page.body.raw_text and not page.body:
#             page.body = [('paragraph', RichText(page.body.raw_text))]
#         if page.body_en.raw_text and not page.body_en:
#             page.body_en = [('paragraph', RichText(page.body_en.raw_text))]
#         if page.body_nl.raw_text and not page.body_nl:
#             page.body_nl = [('paragraph', RichText(page.body_nl.raw_text))]
#         page.save()
#
#
# def convert_to_richtext_theory_article_page(apps, schema_editor):
#     TheoryArticlePage = apps.get_model('articles.TheoryArticlePage')
#
#     for page in TheoryArticlePage.objects.all():
#         if page.body.raw_text is None:
#             raw_text = ''.join([
#                 child.value.source for child in page.body if child.block_type == 'paragraph'
#             ])
#             page.body = raw_text
#         if page.body_en.raw_text is None:
#             raw_text = ''.join([
#                child.value.source for child in page.body_en if child.block_type == 'paragraph'
#             ])
#             page.body_en = raw_text
#         if page.body_nl.raw_text is None:
#             raw_text = ''.join([
#                child.value.source for child in page.body_nl if child.block_type == 'paragraph'
#             ])
#             page.body_nl = raw_text
#         page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20160326_1423'),
    ]

    operations = [
        # migrations.RunPython(
        #     convert_to_streamfield_story_article_page,
        #     convert_to_richtext_story_article_page
        # ),
        # migrations.RunPython(
        #     convert_to_streamfield_report_article_page,
        #     convert_to_richtext_report_article_page
        # ),
        # migrations.RunPython(
        #     convert_to_streamfield_theory_article_page,
        #     convert_to_richtext_theory_article_page
        # ),
    ]
