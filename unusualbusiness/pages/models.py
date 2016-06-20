from __future__ import unicode_literals

from itertools import chain

from django.db import models
from django.db.models import TextField, SlugField, Model
from django.shortcuts import render
from modelcluster.fields import ParentalKey
from taggit.models import Tag
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from django.db.models import Model, CharField, URLField
from django.utils.translation import ugettext as _
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore import blocks
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from unusualbusiness.utils.models import Heading2Block, Heading3Block, Heading4Block, \
    PullQuoteBlock, FeaturedImageBlock, FeaturedVideoBlock, FeaturedAudioBlock

from unusualbusiness.articles.models import TheoryArticlePage, NewsArticlePage, StoryArticlePage
from unusualbusiness.events.models import EventPage
from unusualbusiness.howtos.models import HowToPage
from unusualbusiness.organizations.models import OrganizationPage


class HomePage(Page):
    subpage_types = [
        'articles.StoryArticleIndexPage',
        'articles.TheoryArticleIndexPage',
        'articles.ActivityIndexPage',
        'articles.AuthorIndexPage',
        'definitions.DefinitionIndexPage',
        'organizations.OrganizationIndexPage',
        'howtos.HowToIndexPage',
        'pages.GeneralPage',
    ]

    def serve(self, request):

        return render(request, self.template, {
            'page': self,
            'articles': HomePage.pages(),
            'featured_articles': HomePage.featured_articles(),
            'upcoming_event': EventPage.upcoming_event(),
            'how_tos': HowToPage.objects.all().live(),
        })

    content_panels = Page.content_panels + [
        InlinePanel('static_content_placements', label="Static Content"),
    ]

    @staticmethod
    def pages():
        theory_article_page_list = TheoryArticlePage.objects.all().live()
        story_article_page_list = StoryArticlePage.objects.all().live()
        news_article_page_list = NewsArticlePage.objects.all().live()
        event_page_list = EventPage.objects.all().live()
        organization_page_list = OrganizationPage.objects.all().live()

        return sorted(chain(
                theory_article_page_list,
                story_article_page_list,
                news_article_page_list,
                event_page_list,
                organization_page_list
            ),
            key=lambda instance: instance.first_published_at,
            reverse=True)

    @staticmethod
    def featured_articles():
        theory_article_list = TheoryArticlePage.objects.live().filter(is_featured=True)
        story_article_list = StoryArticlePage.objects.live().filter(is_featured=True)
        news_article_list = NewsArticlePage.objects.live().filter(is_featured=True)
        event_list = EventPage.objects.live().filter(is_featured=True)

        return sorted(chain(
            theory_article_list,
            story_article_list,
            news_article_list,
            event_list
        ),
            key=lambda instance: instance.first_published_at,
            reverse=True)

        # dutch_content_panels = [
    #     FieldPanel('title_nl', classname="full"),
    #     FieldPanel('body_nl', classname="full"),
    #     StreamFieldPanel('stream_nl'),
    # ]
    #
    # promote_panels = Page.promote_panels + [
    #     ImageChooserPanel('feed_image'),
    #     FieldPanel('date'),
    # ]
    #
    # edit_handler = TabbedInterface([
    #     ObjectList(content_panels, heading='English'),
    #     ObjectList(dutch_content_panels, heading='Nederlands'),
    #     ObjectList(Page.promote_panels, heading='Promote'),
    #     ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    # ])

    # Parent page / subpage type rules


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

    parent_page_types = ['pages.HomePage']
    subpage_types = ['pages.GeneralPage']

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


class HomePageStaticContentPlacement(Orderable, Model):
    home_page = ParentalKey('pages.HomePage', related_name='static_content_placements')
    static_content = models.ForeignKey('pages.StaticContent', related_name='+')

    class Meta:
        verbose_name = "Static content placement"
        verbose_name_plural = "Static content placements"

    panels = [
        SnippetChooserPanel('static_content'),
    ]

    def __str__(self):              # __unicode__ on Python 2
        return self.home_page.title + " -> " + self.static_content.body


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
