from .models import GeneralPage, HomePage, StaticContent
from wagtail_modeltranslation.translator import TranslationOptions
from wagtail_modeltranslation.decorators import register


@register(HomePage)
class HomePageTR(TranslationOptions):
    fields = (
        'title',
        'slug',
    )


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
