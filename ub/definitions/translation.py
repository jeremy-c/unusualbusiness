from .models import DefinitionPage, DefinitionIndexPage
from wagtail_modeltranslation.translation import TranslationOptions
from wagtail_modeltranslation.decorators import register


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
