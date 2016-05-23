from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils.translation import ugettext as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.models import ClusterableModel
from taggit.models import TaggedItemBase, GenericUUIDTaggedItemBase, Tag, CommonGenericTaggedItemBase
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from unusualbusiness.tags.models import EventPageTag
from unusualbusiness.utils.models import RenderInlineMixin, PageFormat


class EventPage(Page, RenderInlineMixin):
    ajax_template = 'events/blocks/inline_event.html'
    format = models.CharField(
        verbose_name=_('page_format'),
        max_length=32,
        null=False,
        default=PageFormat.EVENT,
        choices=PageFormat.ALL)
    event_type = models.CharField(
        verbose_name = _("Type of event"),
        max_length=512,
        blank=True
    )
    is_featured = models.BooleanField(
        verbose_name = _("Is Featured on home page"),
        default=False
    )
    start_date = models.DateTimeField(
        verbose_name=_("Starting date"),
        null=True
    )
    end_date = models.DateTimeField(
        verbose_name=_("End date"),
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
        null=True,
        blank=True
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

    search_fields = Page.search_fields + [
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('description_en'),
        index.SearchField('description_nl'),
        index.SearchField('event_type'),
        index.FilterField('start_date'),
        index.RelatedFields('event_article_page', [
            index.SearchField('title'),
        ]),
        index.RelatedFields('how_to_page', [
            index.SearchField('title'),
        ]),
    ]

    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('is_featured'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('event_type'),
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
    parent_page_types = ['articles.ActivityIndexPage']
    subpage_types = []

    # Methods
    @staticmethod
    def upcoming_events():
        return EventPage.objects.live().filter(start_date__gt=datetime.datetime.now())
