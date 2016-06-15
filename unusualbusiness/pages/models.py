from __future__ import unicode_literals

from django.db import models
from django.db.models import CharField, URLField, TextField, SlugField
from django.db.models import Model
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.wagtailcore import blocks
from django.utils.translation import ugettext as _
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

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
        InlinePanel('static_content_placements', label="Static Content"),
    ]


class GeneralPageStaticContentPlacement(Orderable, models.Model):
    general_page = ParentalKey('pages.GeneralPage', related_name='static_content_placements')
    static_content = models.ForeignKey('pages.StaticContent', related_name='+')

    class Meta:
        verbose_name = "Static content placement"
        verbose_name_plural = "Static content placements"

    panels = [
        SnippetChooserPanel('static_content'),
    ]

    def __str__(self):              # __unicode__ on Python 2
        return self.general_page.title + " -> " + self.static_content.body


# Snippets


@register_snippet
class StaticContent(Model):
    title = CharField(
        verbose_name=_('Title'),
        max_length=255,
        help_text=_("Title of HTML content"),
        blank=False)
    slug = SlugField(
        verbose_name=_('Slug'),
        max_length=255,
        help_text=_("Slug of HTML content"),
        blank=False)
    body = TextField(
        verbose_name=_('HTML Body'),
        help_text=_("Static HTML content for placement in pages"),
        blank=False)

    panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = _("Static content")
        verbose_name_plural = _("Static contents")

    def __str__(self):  # __unicode__ on Python 2
        return self.title

    search_fields = [
        index.SearchField('body', partial_match=True),
    ]


@register_snippet
class Quote(Model):
    quote = CharField(
        verbose_name=_('Quote'),
        max_length=255,
        help_text=_("A quote from an article."),
        blank=False)
    author = CharField(
        verbose_name=_('Attribution'),
        max_length=255,
        help_text=_("Whom is this quote attributed to."),
        blank=True)
    link = URLField(
        verbose_name=_('Link'),
        max_length=255,
        help_text=_("Click quote to go to link."),
        null=True,
        blank=True)

    panels = [
        FieldPanel('quote'),
        FieldPanel('author'),
        FieldPanel('link'),
    ]

    class Meta:
        verbose_name = _("Quote")
        verbose_name_plural = _("Quotes")

    def __str__(self):  # __unicode__ on Python 2
        return self.quote

    search_fields = [
        index.SearchField('quote', partial_match=True),
        index.SearchField('author', partial_match=True),
    ]
