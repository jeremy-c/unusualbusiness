from .models import HowToPage, HowToIndexPage
from wagtail_modeltranslation.translator import TranslationOptions
from wagtail_modeltranslation.decorators import register


@register(HowToPage)
class HowToPageTR(TranslationOptions):
    fields = (
        'title',
        'slug',
        'description',
    )


@register(HowToIndexPage)
class HowToIndexPageTR(TranslationOptions):
    fields = (
    )