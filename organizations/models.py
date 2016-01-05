from __future__ import unicode_literals

from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, TabbedInterface, ObjectList, \
    StreamFieldPanel
from wagtail.wagtailcore.fields import RichTextField, StreamField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail_modeltranslation.models import TranslationMixin
from wagtail.wagtailsearch import index
from wagtail.wagtailcore import blocks


class OrganizationPage(TranslationMixin, Page):

    # Database fields

    description = RichTextField()
    date_founded = models.DateField("Founded date")
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Search index configuraiton

    search_fields = Page.search_fields + (
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('description_en'),
        index.SearchField('description_nl'),
        index.FilterField('date_founded'),
    )


    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('date_founded'),
        FieldPanel('description_en', classname="full"),
        FieldPanel('description_nl', classname="full"),
    ]
    #
    # dutch_content_panels = [
    #     FieldPanel('title_nl', classname="full"),
    #     FieldPanel('description_nl', classname="full"),
    # ]
    #
    # promote_panels = [
    #     MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    #     ImageChooserPanel('feed_image'),
    # ]
    #
    # edit_handler = TabbedInterface([
    #     ObjectList(content_panels, heading='English'),
    #     ObjectList(dutch_content_panels, heading='Nederlands'),
    #     ObjectList(Page.promote_panels, heading='Promote'),
    #     ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    # ])

    # Parent page / subpage type rules]
    parent_page_types = ['organizations.OrganizationIndexPage']
    subpage_types = []


class OrganizationIndexPage(TranslationMixin, Page):

    # content_panels = Page.content_panels + [
    # ]
    #
    # dutch_content_panels = [
    #     FieldPanel('title_nl', classname="full"),
    # ]
    #
    # promote_panels = [
    #     MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    #     FieldPanel('slug_nl'),
    # ]
    #
    # edit_handler = TabbedInterface([
    #     ObjectList(content_panels, heading='English'),
    #     ObjectList(dutch_content_panels, heading='Nederlands'),
    #     ObjectList(Page.promote_panels, heading='Promote'),
    #     ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    # ])

    subpage_types = ['organizations.OrganizationPage']

    def get_context(self, request):
        context = super(OrganizationIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['organizations'] = OrganizationPage.objects.child_of(self).live()
        return context
