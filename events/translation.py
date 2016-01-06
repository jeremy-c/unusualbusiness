from .models import OrganizationPage, OrganizationIndexPage
from wagtail_modeltranslation.translator import TranslationOptions
from wagtail_modeltranslation.decorators import register


@register(EventPage)
class EventPageTR(TranslationOptions):
    fields = (
        'title',
        'slug',
        'description',
    )


@register(EventIndexPage)
class EventIndexPageTR(TranslationOptions):
    fields = (
    )