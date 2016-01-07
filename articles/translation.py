# translation.py
from .models import StoryArticlePage, TheoryArticlePage, ReportArticlePage
from wagtail_modeltranslation.translation import TranslationOptions
from wagtail_modeltranslation.decorators import register


@register(StoryArticlePage)
class StoryArticlePageTR(TranslationOptions):
 fields = (
    'title',
    'subtitle',
    'summary',
    'body',
 )


@register(TheoryArticlePage)
class TheoryArticlePageTR(TranslationOptions):
 fields = (
    'title',
    'subtitle',
    'summary',
    'body',
 )


@register(ReportArticlePage)
class ReportArticlePageTR(TranslationOptions):
 fields = (
    'title',
    'subtitle',
    'summary',
    'body',
 )

