# translation.py
from .models import ArticlePage
from wagtail_modeltranslation.translation import TranslationOptions
from wagtail_modeltranslation.decorators import register

@register(ArticlePage)
class ArticlePageTR(TranslationOptions):
 fields = (
    'title',
    'subtitle',
    'summary',
    'body',
 )
