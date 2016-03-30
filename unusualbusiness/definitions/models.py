from django.db import models
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, TabbedInterface, ObjectList, \
    StreamFieldPanel
from wagtail_modeltranslation.models import TranslationMixin
from unusualbusiness.utils.models import RenderInlineMixin


# Create your models here.


class DefinitionPage(TranslationMixin, Page, RenderInlineMixin):
    ajax_template = 'definitions/blocks/inline_definition.html'

    #TODO: add bold and italic to Wysiwyg
    definition = models.TextField(null=True, blank=True)

    parent_page_types = ['definitions.DefinitionIndexPage']

    def __str__(self):              # __unicode__ on Python 2
        return self.title

DefinitionPage.content_panels = Page.content_panels + [
        FieldPanel('definition'),
    ]
DefinitionPage.promote_panels = Page.promote_panels


class DefinitionIndexPage(TranslationMixin, Page):

    parent_page_types = ['home.HomePage']
    subpage_types = ['definitions.DefinitionPage']

    def get_context(self, request):
        context = super(DefinitionIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['definitions'] = DefinitionPage.objects.child_of(self).live()
        return context
