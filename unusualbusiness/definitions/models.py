from django.db import models
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from unusualbusiness.utils.models import RenderInlineMixin, PageFormat
from django.utils.translation import ugettext as _


class DefinitionPage(Page, RenderInlineMixin):
    ajax_template = 'definitions/blocks/inline_definition.html'
    format = models.CharField(
        verbose_name=_('page_format'),
        max_length=32,
        null=False,
        default=PageFormat.THEORY,
        choices=PageFormat.ALL)
    #TODO: add bold and italic to Wysiwyg
    definition = models.TextField(null=True, blank=True)

    parent_page_types = ['definitions.DefinitionIndexPage']

    def __str__(self):              # __unicode__ on Python 2
        return self.title

DefinitionPage.content_panels = Page.content_panels + [
        FieldPanel('definition'),
    ]
DefinitionPage.promote_panels = Page.promote_panels


class DefinitionIndexPage(Page):

    parent_page_types = ['pages.HomePage']
    subpage_types = ['definitions.DefinitionPage']

    def get_context(self, request):
        context = super(DefinitionIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['definitions'] = DefinitionPage.objects.child_of(self).live()
        return context
