from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase, CommonGenericTaggedItemBase, GenericUUIDTaggedItemBase, Tag
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from unusualbusiness.events.models import EventPage
from unusualbusiness.organizations.models import OrganizationPage
from unusualbusiness.tags.models import TheoryArticlePageTag, StoryArticlePageTag, NewsArticlePageTag
from unusualbusiness.utils.models import PageFormat, RenderInlineMixin


class TheoryArticleIndexPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['articles.TheoryArticlePage']

    def get_context(self, request):
        context = super(TheoryArticleIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['articles'] = TheoryArticlePage.objects.all().live()
        context['parent'] = self.get_parent()
        return context


class StoryArticleIndexPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['articles.StoryArticlePage']

    def get_context(self, request):
        context = super(StoryArticleIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['articles'] = StoryArticlePage.objects.all().live()
        context['parent'] = self.get_parent()
        return context


class ActivityIndexPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['events.EventPage', 'articles.NewsArticlePage', ]

    def get_context(self, request):
        context = super(ActivityIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['events'] = EventPage.objects.child_of(self).live()
        context['news'] = NewsArticlePage.objects.child_of(self).live()
        return context


class Heading2Block(blocks.StructBlock):
    chapter_name = \
        blocks.CharBlock(required=True)

    class Meta:
        template = 'articles/blocks/heading2.html'
        icon = 'title'
        label = _('Chapter (h2)')


class Heading3Block(blocks.StructBlock):
    section_name = blocks.CharBlock(required=True)

    class Meta:
        template = 'articles/blocks/heading3.html'
        icon = 'title'
        label = _('Section (h3)')


class Heading4Block(blocks.StructBlock):
    subsection_name = blocks.CharBlock(required=True)

    class Meta:
        template = 'articles/blocks/heading4.html'
        icon = 'title'
        label = _('Subsection (h4)')


class PullQuoteBlock(blocks.StructBlock):
    pull_quote = blocks.CharBlock(required=True)

    class Meta:
        template = 'articles/blocks/pullquote.html'
        icon = 'openquote'
        label = 'Pull Quote'


class FeaturedImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)

    class Meta:
        icon='image'
        label=_('Image')
        template='articles/blocks/featured_image.html'
        help_text=_('The featured image is shown in the list-view and detail-view')


class FeaturedVideoBlock(blocks.StructBlock):
    video = EmbedBlock(required=True)

    class Meta:
        icon='media'
        label=_('Video')
        template='articles/blocks/featured_video.html'
        help_text=_('The featured video is only shown in the detail-view, make sure to also selecte a featured image')


class FeaturedAudioBlock(blocks.StructBlock):
    audio = EmbedBlock(required=True)

    class Meta:
        icon='media'
        label=_('Audio')
        template='articles/blocks/featured_audio.html'
        help_text=_('The featured audio is only shown in the detail-view, make sure to also selecte a featured image')


class AbstractArticle(models.Model, RenderInlineMixin):
    is_featured = models.BooleanField(
        verbose_name = _("Is Featured on home page"),
        default=False
    )
    subtitle = models.CharField(
        verbose_name=_('subtitle'),
        max_length=255,
        help_text=_("The subtitle of the page"),
        blank=True
    )
    format = models.CharField(
        verbose_name=_('page_format'),
        max_length=32,
        null=False,
        default = PageFormat.TEXT,
        choices=PageFormat.ALL)
    featured = StreamField([
        ('featured_image', FeaturedImageBlock()),
        ('featured_video', FeaturedVideoBlock()),
        ('featured_audio', FeaturedAudioBlock()),
    ])
    author = models.ForeignKey(
        'articles.AuthorPage',
        verbose_name=_('author'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    publication_date = models.DateTimeField(
        verbose_name=_('publication_date'),
        help_text=_("The publication date of the article"),
        default=timezone.now,
        blank=True,
        null=True,
    )
    body = StreamField([
        ('introduction', blocks.RichTextBlock(icon="italic")),
        ('chapter', Heading2Block()),
        ('section', Heading3Block()),
        ('subsection', Heading4Block()),
        ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
        # ('markdown_paragraph', MarkdownBlock(icon="code")),
        ('image', ImageChooserBlock(icon="image")),
        ('pullquote', PullQuoteBlock()),
        ('embed', EmbedBlock()),
    ])

    class Meta:
        abstract = True
        verbose_name = _("Article")

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


class AbstractHowToArticleMixin(object):
    def __init__(self):
        pass

    def related_how_tos(self):
        return [related_how_to_page.how_to_page
                   for related_how_to_page
                   in self.how_to_page.select_related().all()]

    def related_how_to_story_articles(self, related_how_tos=None):
        if related_how_tos is None:
            related_how_tos = self.related_how_tos()

        how_to_story_articles_list = []
        for related_how_to in related_how_tos:
            how_to_story_articles = related_how_to.story_pages()
            self_idx = None

            for idx, story in enumerate(how_to_story_articles):
                if story.id is self.id:
                    self_idx = idx

            previous_article_idx = self_idx - 1
            next_article_idx = self_idx + 1
            previous_article = None
            next_article = None

            if 0 <= previous_article_idx < len(how_to_story_articles):
                previous_article = how_to_story_articles[previous_article_idx]

            if 0 <= next_article_idx < len(how_to_story_articles):
                next_article = how_to_story_articles[next_article_idx]

            how_to_story_articles_list.append({
                related_how_to,
                (previous_article, next_article)
            })

        return how_to_story_articles_list

    def upcoming_related_event_pages(self, related_how_tos=None):
        if related_how_tos is None:
            related_how_tos = self.related_how_tos()

        how_to_events = [how_to_page.events()
                 for how_to_page
                 in related_how_tos]

        event_pages = []
        for how_to_event in how_to_events:
            how_to_event = how_to_event.first()
            if how_to_event and how_to_event.event.is_upcoming:
                event_pages.append(how_to_event.event)

        return event_pages

    def related_organizations(self):
        return [related_organization.organization_page
                            for related_organization
                            in self.organizations.select_related().all()]


class StoryArticlePage(Page, AbstractArticle, AbstractHowToArticleMixin):
    parent_page_types = ['articles.StoryArticleIndexPage']
    subpage_types = []

    tags = ClusterTaggableManager(through=StoryArticlePageTag, blank=True)

    class Meta:
        verbose_name = _("Story")
        verbose_name_plural = _("Stories")

    def get_context(self, request):
        context = super(StoryArticlePage, self).get_context(request)

        related_how_tos = self.related_how_tos()

        context['how_tos'] = related_how_tos
        context['upcoming_related_events'] = self.upcoming_related_event_pages(related_how_tos)
        context['related_how_to_story_articles'] = self.related_how_to_story_articles(related_how_tos)

        return context

StoryArticlePage.content_panels = Page.content_panels + [
        FieldPanel('is_featured'),
        FieldPanel('subtitle'),
        PageChooserPanel('author', page_type='articles.AuthorPage'),
        FieldPanel('format'),
        FieldPanel('publication_date'),
        StreamFieldPanel('featured'),
        StreamFieldPanel('body'),
        InlinePanel('organizations', label=_("Organizations")),
        FieldPanel('tags'),
    ]

StoryArticlePage.promote_panels = Page.promote_panels

StoryArticlePage.search_fields = Page.search_fields + [
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('subtitle_en'),
        index.SearchField('subtitle_nl'),
        index.SearchField('body_en'),
        index.SearchField('body_nl'),
        index.RelatedFields('organizations', [
            index.SearchField('title'),
        ]),
        index.RelatedFields('how_to_page', [
            index.SearchField('title'),
        ]),
        index.RelatedFields('author', [
            index.SearchField('title'),
        ]),
    ]


class StoryArticlePageOrganization(Orderable, models.Model):
    story_article_page = ParentalKey('articles.StoryArticlePage', related_name='organizations')
    organization_page = models.ForeignKey(
        'organizations.OrganizationPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='story_article_page'
    )

    panels = [
          PageChooserPanel('organization_page'),
    ]

    def __str__(self):              # __unicode__ on Python 2
        return self.story_article_page.title + " -> " + self.organization_page.title


class TheoryArticlePage(Page, AbstractArticle, AbstractHowToArticleMixin):
    ajax_template = 'articles/blocks/inline_theory_article.html'
    parent_page_types = ['articles.TheoryArticleIndexPage']
    subpage_types = []

    tags = ClusterTaggableManager(through=TheoryArticlePageTag, blank=True)

    class Meta:
        verbose_name = _("Theory")
        verbose_name_plural = _("Theories")

TheoryArticlePage.content_panels = Page.content_panels + [
        FieldPanel('is_featured'),
        FieldPanel('subtitle'),
        PageChooserPanel('author', page_type='articles.AuthorPage'),
        FieldPanel('format'),
        StreamFieldPanel('featured'),
        FieldPanel('publication_date'),
        StreamFieldPanel('body'),
        FieldPanel('tags'),
    ]

TheoryArticlePage.promote_panels = Page.promote_panels

TheoryArticlePage.search_fields = Page.search_fields + [
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('subtitle_en'),
        index.SearchField('subtitle_nl'),
        index.SearchField('body_en'),
        index.SearchField('body_nl'),
        index.RelatedFields('how_to_page', [
            index.SearchField('title'),
        ]),
        index.RelatedFields('author', [
          index.SearchField('title'),
        ]),
    ]


class NewsArticlePage(Page, AbstractArticle):
    event_page = models.ForeignKey(
        'events.EventPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='news_article_page'
    )
    tags = ClusterTaggableManager(through=NewsArticlePageTag, blank=True)

    parent_page_types = ['events.EventPage', 'articles.ActivityIndexPage']
    subpage_types = []

    class Meta:
        verbose_name = _("News or report article")
        verbose_name_plural = _("News or report articles")

NewsArticlePage.content_panels = Page.content_panels + [
        FieldPanel('is_featured'),
        PageChooserPanel('event_page'),
        FieldPanel('subtitle'),
        PageChooserPanel('author', page_type='articles.AuthorPage'),
        FieldPanel('format'),
        StreamFieldPanel('featured'),
        FieldPanel('publication_date'),
        StreamFieldPanel('body'),
        FieldPanel('tags'),
    ]

NewsArticlePage.promote_panels = Page.promote_panels

NewsArticlePage.search_fields = Page.search_fields + [
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('subtitle_en'),
        index.SearchField('subtitle_nl'),
        index.SearchField('body_en'),
        index.SearchField('body_nl'),
        index.RelatedFields('event_page', [
            index.SearchField('title'),
        ]),
        index.RelatedFields('author', [
            index.SearchField('title'),
        ]),
    ]


class AuthorPage(Page):
    photo = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('photo'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    biography = models.TextField(
        verbose_name=_('biography'),
        help_text=_("The biography of the author (max. 150 woorden)"),
        blank=True
    )

    parent_page_types = ['articles.AuthorIndexPage']
    subpage_types = []

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

AuthorPage.content_panels = Page.content_panels + [
    FieldPanel('biography'),
    ImageChooserPanel('photo'),
]

AuthorPage.promote_panels = Page.promote_panels


class AuthorIndexPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['articles.AuthorPage']

    def get_context(self, request):
        context = super(AuthorIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['authors'] = AuthorPage.objects.all().live()
        context['parent'] = self.get_parent()
        return context

