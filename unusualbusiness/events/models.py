from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.utils.translation import ugettext as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase, GenericUUIDTaggedItemBase, Tag, CommonGenericTaggedItemBase
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, TabbedInterface, ObjectList, \
    StreamFieldPanel, PageChooserPanel
from wagtail.wagtailcore.fields import RichTextField, StreamField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail_modeltranslation.models import TranslationMixin
from wagtail.wagtailsearch import index
from wagtail.wagtailcore import blocks

from unusualbusiness.tags.models import EventPageTag
from unusualbusiness.utils.models import RenderInlineMixin


class EventPage(TranslationMixin, Page, RenderInlineMixin):
    ajax_template = 'events/blocks/inline_event.html'

    start_date = models.DateTimeField(
        verbose_name = _("Starting date"),
    )
    end_date = models.DateTimeField(
        verbose_name = _("End date"),
        null=True,
        blank=True
    )
    # This should probably be a specific geolocation field:
    location = models.CharField(
        verbose_name = _("Location"),
        max_length=512,
        blank=True
    )
    # TODO: Add participating groups as ForeignKeys
    description = RichTextField(
        verbose_name = _("Description"),
        null=True
    )
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name = _("Featured image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    poster_link = models.URLField(
        verbose_name = _("Poster"),
        blank=True
    )
    flyer_link = models.URLField(
        verbose_name = _("Flyer"),
        blank=True
    )
    facebook_event = models.URLField(
        verbose_name = _("Facebook event"),
        blank=True
    )
    tags = ClusterTaggableManager(through=EventPageTag, blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('description_en'),
        index.SearchField('description_nl'),
        index.FilterField('start_date'),
        index.RelatedFields('report_article_page', [
            index.SearchField('title'),
        ]),
        index.RelatedFields('how_to_page', [
            index.SearchField('title'),
        ]),
    )

    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('location'),
        FieldPanel('description_en', classname="full"),
        FieldPanel('description_nl', classname="full"),
        ImageChooserPanel('featured_image'),
        FieldPanel('poster_link'),
        FieldPanel('flyer_link'),
        FieldPanel('facebook_event'),
        FieldPanel('tags'),
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
    parent_page_types = ['events.EventIndexPage']
    subpage_types = ['articles.ReportArticlePage']

    # Methods
    @staticmethod
    def upcoming_events():
        return EventPage.objects.all().filter(start_date__gt=datetime.now).live()


class EventIndexPage(TranslationMixin, Page):

    parent_page_types = ['home.HomePage']
    subpage_types = ['events.EventPage']

    def get_context(self, request):
        context = super(EventIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['events'] = EventPage.objects.child_of(self).live()
        return context
