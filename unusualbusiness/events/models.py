from __future__ import unicode_literals

from datetime import date, timedelta
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _
from modelcluster.models import ClusterableModel
from taggit.models import TaggedItemBase, GenericUUIDTaggedItemBase, Tag, CommonGenericTaggedItemBase
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from unusualbusiness.utils.models import PageFormat, Heading2Block, Heading3Block, Heading4Block, \
    PullQuoteBlock
from unusualbusiness.utils.models import RenderInlineMixin, RelatedHowToMixin


class EventPage(Page, RenderInlineMixin, RelatedHowToMixin):
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
    venue_name = models.CharField(
        verbose_name=_("Venue"),
        max_length=128,
        blank=True
    )
    # TODO: Geolocation - http://www.tivix.com/blog/using-leaflet-geodjango-geospatial-data/
    venue_address = models.CharField(
        verbose_name=_("Address"),
        max_length=128,
        blank=True
    )
    venue_postal_code = models.CharField(
        verbose_name=_("Postal code"),
        max_length=8,
        blank=True
    )
    venue_city = models.CharField(
        verbose_name=_("City"),
        max_length=64,
        blank=True
    )
    venue_country = models.CharField(
        verbose_name=_("Country"),
        max_length=64,
        blank=True
    )
    description = StreamField([
        ('introduction', blocks.TextBlock(icon="italic", rows=3)),
        ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('pullquote', PullQuoteBlock()),
        ('embed', EmbedBlock()),
        ('chapter', Heading2Block()),
        ('section', Heading3Block()),
        ('subsection', Heading4Block()),
        # ('markdown_paragraph', MarkdownBlock(icon="code")),
    ])
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name = _("Featured image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    facebook_event = models.URLField(
        verbose_name = _("Facebook event"),
        blank=True
    )

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    search_fields = Page.search_fields + [
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('description_en'),
        index.SearchField('description_nl'),
        index.SearchField('event_type'),
        index.FilterField('start_date'),
        index.FilterField('venue_name'),
        index.FilterField('venue_city'),
        index.FilterField('venue_country'),
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
        StreamFieldPanel('description_en'),
        StreamFieldPanel('description_nl'),
        ImageChooserPanel('featured_image'),
        FieldPanel('venue_name'),
        FieldPanel('venue_address'),
        FieldPanel('venue_postal_code'),
        FieldPanel('venue_city'),
        FieldPanel('venue_country'),
        FieldPanel('facebook_event'),
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

    # Properties

    @property
    def is_upcoming(self):
        if self.start_date.date() >= date.today():
            return True
        return False

    @property
    def doors_open_from(self):
        return self.start_date - timedelta(minutes=settings.DOORS_OPEN_MINUTES_BEFORE_START_EVENT)

    @property
    def location(self):
        return ", ".join([self.venue_name,
                          self.venue_address,
                          self.venue_postal_code,
                          self.venue_city,
                          self.venue_country
                          ])

    @property
    def event_report(self):
        return self.news_article_page.first()

    # Static Methods

    @staticmethod
    def upcoming_events():
        return EventPage.objects.live().filter(start_date__gte=date.today())

    @staticmethod
    def upcoming_event():
        return EventPage.upcoming_events().first()

    #  Methods

    def get_context(self, request):
        context = super(EventPage, self).get_context(request)

        context['event_report'] = self.event_report
        context['related_events'] = self.related_how_to_events(self_idx=self.id)
        context['parent'] = self.get_parent()

        return context
