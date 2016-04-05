from django.template.loader import get_template
from wagtail.wagtailcore.models import Page
from wagtail_modeltranslation.models import TranslationMixin
from django.utils.translation import ugettext as _


class RenderInlineMixin():
    def __init__(self):
        pass

    def render_inline(self):
        template = get_template(self.ajax_template)
        return template.render({
            'self': self
        })

DOCUMENT_FORMAT = (
    ('event',       _('Event')),
    ('video',       _('Video')),
    ('text',        _('Text')),
    ('images',      _('Image slideshow')),
    ('audio',       _('Audio embed')),
    ('organization',_('Organization')),
    ('theory',      _('Theory')),
    ('link',        _('External link')),
    ('document',    _('Document download'))
)
