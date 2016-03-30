from django.template.loader import get_template
from wagtail.wagtailcore.models import Page
from wagtail_modeltranslation.models import TranslationMixin


class RenderInlineMixin():
    def render_inline(self):
        template = get_template(self.ajax_template)
        return template.render({
            'self': self
        })
