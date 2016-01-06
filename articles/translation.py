# translation.py
from .models import StoryArticlePage, TheoryArticlePage, ReportArticlePage, DefinitionPage, DefinitionIndexPage
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


@register(DefinitionPage)
class DefinitionPageTR(TranslationOptions):
 fields = (
    'title',
    'definition',
 )


@register(DefinitionIndexPage)
class DefinitionIndexPageTR(TranslationOptions):
 fields = (
 )
