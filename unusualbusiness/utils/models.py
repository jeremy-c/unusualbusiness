from django.db.models import Model
from django.template.loader import get_template
from django_choices_enum import ChoicesEnum
from wagtail.wagtailcore.models import Page
from wagtail_modeltranslation.models import TranslationMixin
from django.utils.translation import ugettext as _


class RenderInlineMixin(object):
    def __init__(self):
        pass

    def render_inline(self):
        template = get_template(self.ajax_template)
        return template.render({
            'self': self
        })


class PageFormat:
    EVENT = 'event'
    VIDEO = 'video'
    TEXT = 'text'
    IMAGES = 'images'
    AUDIO = 'audio',
    ORGANIZATION = 'organization'
    THEORY = 'theory'
    LINK = 'link'
    DOCUMENT = 'document'

    ALL = (
        (TEXT, _('Normal Article')),
        (THEORY, _('Theory Article')),
        (VIDEO, _('Video embed')),
        (AUDIO, _('Audio embed')),
        (IMAGES, _('Image slideshow')),
        (EVENT, _('Event')),
        (ORGANIZATION, _('Organization')),
        (LINK, _('External Link')),
        (DOCUMENT, _('Document Download')),
    )

    def __init__(self):
        pass
