from __future__ import unicode_literals

from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore import blocks
from django.utils.translation import ugettext as _
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from unusualbusiness.utils.models import FeaturedImageBlock, FeaturedAudioBlock, PullQuoteBlock, Heading2Block, \
    Heading3Block, Heading4Block
from unusualbusiness.utils.models import FeaturedVideoBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class GeneralPage(Page):
    is_featured = models.BooleanField(
        verbose_name=_("Is Featured on home page"),
        default=False
    )
    featured = StreamField([
        ('featured_image', FeaturedImageBlock()),
        ('featured_video', FeaturedVideoBlock()),
        ('featured_audio', FeaturedAudioBlock()),
    ])
    body = StreamField([
        ('introduction', blocks.RichTextBlock(icon="italic")),
        ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
        # ('markdown_paragraph', MarkdownBlock(icon="code")),
        ('image', ImageChooserBlock(icon="image")),
        ('pullquote', PullQuoteBlock()),
        ('embed', EmbedBlock()),
        ('chapter', Heading2Block()),
        ('section', Heading3Block()),
        ('subsection', Heading4Block()),
    ])

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")

    def __featured_item(self, block_type='featured_image'):
        for stream_child in self.featured:
            if stream_child.block_type == block_type:
                return stream_child
        return None

    @property
    def featured_image(self):
        return self.__featured_item('featured_image')

    @property
    def featured_audio(self):
        return self.__featured_item('featured_audio')

    @property
    def featured_video(self):
        return self.__featured_item('featured_video')

    @property
    def introduction(self):
        for stream_child in self.body:
            if stream_child.block_type == 'introduction':
                return stream_child.value.source
        return None

    def get_context(self, request):
        context = super(GeneralPage, self).get_context(request)
        return context

    subpage_types = [
        'pages.GeneralPage',
    ]

    search_fields = Page.search_fields + [
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('body_en'),
        index.SearchField('body_nl'),
    ]

    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('is_featured'),
        StreamFieldPanel('featured'),
        StreamFieldPanel('body_en'),
        StreamFieldPanel('body_nl'),
    ]
