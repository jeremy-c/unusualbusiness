from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase, CommonGenericTaggedItemBase, GenericUUIDTaggedItemBase, Tag
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail_modeltranslation.models import TranslationMixin

from wagtail.wagtailcore import blocks

from unusualbusiness.events.models import EventPage
from unusualbusiness.organizations.models import OrganizationPage
from unusualbusiness.tags.models import TheoryArticlePageTag, StoryArticlePageTag, ReportArticlePageTag
from unusualbusiness.utils.models import PageFormat


class TheoryArticleIndexPage(TranslationMixin, Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['articles.TheoryArticlePage']

    def get_context(self, request):
        context = super(TheoryArticleIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['articles'] = TheoryArticlePage.objects.all().live()
        context['parent'] = self.get_parent()
        return context


class StoryArticleIndexPage(TranslationMixin, Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['articles.StoryArticlePage']

    def get_context(self, request):
        context = super(StoryArticleIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['articles'] = StoryArticlePage.objects.all().live()
        context['parent'] = self.get_parent()
        return context


class PullQuoteBlock(blocks.StructBlock):
    pull_quote = blocks.CharBlock(required=True)

    class Meta:
        template = 'articles/blocks/pullquote.html'
        icon = 'openquote'
        label = 'Pull Quote'


class CarouselBlock(blocks.StreamBlock):
    image = ImageChooserBlock()
    embed = EmbedBlock()

    class Meta:
        template = 'articles/blocks/carousel.html'
        icon = 'media'
        label = 'Carousel'


class AbstractArticle(models.Model):
    subtitle = models.CharField(
        verbose_name=_('subtitle'),
        max_length=255,
        help_text=_("The subtitle of the page"),
        blank=True
    )
    format = models.CharField(
        verbose_name=_('page_format'),
        max_length=16,
        null=False,
        default = PageFormat.TEXT,
        choices=PageFormat.ALL)
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('featured_image'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    author = models.ForeignKey(
        'articles.AuthorPage',
        verbose_name=_('author'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    summary = models.TextField(
        verbose_name=_('summary'),
        help_text=_("The summary of the articles (max 100 words)"),
        blank=True
    )
    publication_date = models.DateTimeField(
        verbose_name=_('publication_date'),
        help_text=_("The publication date of the article"),
        default=timezone.now,
        blank=True,
        null=True,
    )
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('pullquote', PullQuoteBlock()),
        ('carousel', CarouselBlock())
    ])

    class Meta:
        abstract = True
        verbose_name = _("Article")


class StoryArticlePage(TranslationMixin, Page, AbstractArticle):
    parent_page_types = ['articles.StoryArticleIndexPage']
    subpage_types = []

    tags = ClusterTaggableManager(through=StoryArticlePageTag, blank=True)

    class Meta:
        verbose_name = _("Story")
        verbose_name_plural = _("Stories")

    def get_context(self, request):
        context = super(StoryArticlePage, self).get_context(request)
        # Add extra variables and return the updated context

        how_tos = [related_how_to_page.how_to_page for related_how_to_page in self.how_to_page.select_related().all()]
        related_story_pages =[how_to_page.story_pages() for how_to_page in how_tos]

        story_article_pages = []
        for related_story_page in related_story_pages:
            story_article_pages.append(related_story_page.first().article)

        how_to_events = [how_to_page.events() for how_to_page in how_tos]
        event_pages = []
        for how_to_event in how_to_events:
            how_to_event = how_to_event.first()
            if how_to_event:
                event_pages.append(how_to_event.event)

        organizations = [related_organization.organization_page for related_organization in self.organizations.select_related().all()]

        context['organizations'] = organizations
        context['events'] = event_pages
        context['how_tos'] = how_tos
        context['related_articles'] = story_article_pages

        return context

StoryArticlePage.content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        PageChooserPanel('author', page_type='articles.AuthorPage'),
        FieldPanel('format'),
        ImageChooserPanel('featured_image'),
        FieldPanel('summary'),
        FieldPanel('publication_date'),
        StreamFieldPanel('body'),
        InlinePanel('organizations', label=_("Organizations")),
        FieldPanel('tags'),
    ]



StoryArticlePage.promote_panels = Page.promote_panels

StoryArticlePage.search_fields = Page.search_fields + (
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('subtitle_en'),
        index.SearchField('subtitle_nl'),
        index.SearchField('summary_en'),
        index.SearchField('summary_nl'),
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
    )


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


class TheoryArticlePage(TranslationMixin, Page, AbstractArticle):
    parent_page_types = ['articles.TheoryArticleIndexPage']
    subpage_types = []

    tags = ClusterTaggableManager(through=TheoryArticlePageTag, blank=True)

    class Meta:
        verbose_name = _("Theory")
        verbose_name_plural = _("Theories")

TheoryArticlePage.content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        PageChooserPanel('author', page_type='articles.AuthorPage'),
        FieldPanel('format'),
        ImageChooserPanel('featured_image'),
        FieldPanel('summary'),
        FieldPanel('publication_date'),
        StreamFieldPanel('body'),
        FieldPanel('tags'),
    ]

TheoryArticlePage.promote_panels = Page.promote_panels

TheoryArticlePage.search_fields = Page.search_fields + (
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('subtitle_en'),
        index.SearchField('subtitle_nl'),
        index.SearchField('summary_en'),
        index.SearchField('summary_nl'),
        index.SearchField('body_en'),
        index.SearchField('body_nl'),
        index.RelatedFields('how_to_page', [
            index.SearchField('title'),
        ]),
        index.RelatedFields('author', [
          index.SearchField('title'),
        ]),
    )


class ReportArticlePage(TranslationMixin, Page, AbstractArticle):
    event_page = models.ForeignKey(
        'events.EventPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='report_article_page'
    )
    tags = ClusterTaggableManager(through=ReportArticlePageTag, blank=True)

    parent_page_types = ['events.EventPage']
    subpage_types = []

    class Meta:
        verbose_name = _("Event report")

ReportArticlePage.content_panels = Page.content_panels + [
        PageChooserPanel('event_page'),
        FieldPanel('subtitle'),
        PageChooserPanel('author', page_type='articles.AuthorPage'),
        FieldPanel('format'),
        ImageChooserPanel('featured_image'),
        FieldPanel('summary'),
        FieldPanel('publication_date'),
        StreamFieldPanel('body'),
        FieldPanel('tags'),
    ]

ReportArticlePage.promote_panels = Page.promote_panels

ReportArticlePage.search_fields = Page.search_fields + (
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('subtitle_en'),
        index.SearchField('subtitle_nl'),
        index.SearchField('summary_en'),
        index.SearchField('summary_nl'),
        index.SearchField('body_en'),
        index.SearchField('body_nl'),
        index.RelatedFields('event_page', [
            index.SearchField('title'),
        ]),
        index.RelatedFields('author', [
            index.SearchField('title'),
        ]),

)


class AuthorPage(TranslationMixin, Page):
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


class AuthorIndexPage(TranslationMixin, Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['articles.AuthorPage']

    def get_context(self, request):
        context = super(AuthorIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['authors'] = AuthorPage.objects.all().live()
        context['parent'] = self.get_parent()
        return context

