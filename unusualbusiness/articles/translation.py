# translation.py
from .models import StoryArticlePage, TheoryArticlePage, ReportArticlePage, StoryArticleIndexPage, \
    TheoryArticleIndexPage, AuthorPage, AuthorIndexPage
from wagtail_modeltranslation.translation import TranslationOptions
from wagtail_modeltranslation.decorators import register


@register(StoryArticlePage)
class StoryArticlePageTR(TranslationOptions):
 fields = (
    'title',
    'subtitle',
    'body',
 )


@register(TheoryArticlePage)
class TheoryArticlePageTR(TranslationOptions):
 fields = (
    'title',
    'subtitle',
    'body',
 )


@register(ReportArticlePage)
class ReportArticlePageTR(TranslationOptions):
 fields = (
    'title',
    'subtitle',
    'body',
 )


@register(StoryArticleIndexPage)
class StoryArticleIndexPageTR(TranslationOptions):
 fields = (
 )


@register(TheoryArticleIndexPage)
class TheoryArticleIndexPageTR(TranslationOptions):
 fields = (
 )

@register(AuthorPage)
class AuthorPageTR(TranslationOptions):
    fields = (
        'biography',
    )


@register(AuthorIndexPage)
class AuthorIndexPageTR(TranslationOptions):
    fields = (
    )
