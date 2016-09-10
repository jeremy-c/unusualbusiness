from .models import EventPage
from wagtail_modeltranslation.translator import TranslationOptions
from wagtail_modeltranslation.decorators import register


@register(EventPage)
class EventPageTR(TranslationOptions):
    fields = (
        'title',
        'slug',
        'description',
        'event_type',
    )
