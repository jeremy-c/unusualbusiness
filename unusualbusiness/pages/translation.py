from .models import GeneralPage, StaticContent
from wagtail_modeltranslation.translator import TranslationOptions
from wagtail_modeltranslation.decorators import register


@register(GeneralPage)
class GeneralPageTR(TranslationOptions):
    fields = (
        'title',
        'body',
        'slug',
    )


@register(StaticContent)
class StaticContentTR(TranslationOptions):
    fields = (
        'body',
    )
