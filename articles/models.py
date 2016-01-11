from __future__ import unicode_literals
from django.utils.translation import ugettext as _

from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase, CommonGenericTaggedItemBase, GenericUUIDTaggedItemBase, Tag
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, TabbedInterface, ObjectList, \
    StreamFieldPanel, PageChooserPanel
from wagtail.wagtailcore.blocks import PageChooserBlock
from wagtail.wagtailcore.fields import RichTextField, StreamField

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.blocks import SnippetChooserBlock
from wagtail.wagtailsnippets.models import register_snippet
from wagtail_modeltranslation.models import TranslationMixin
from wagtail.wagtailsearch import index
from wagtail.wagtailcore import blocks

from events.models import EventPage
from tags.models import TheoryArticlePageTag, StoryArticlePageTag, ReportArticlePageTag


class TheoryArticleIndexPage(TranslationMixin, Page):

    parent_page_types = ['home.HomePage']
    subpage_types = ['articles.TheoryArticlePage']

    def get_context(self, request):
        context = super(TheoryArticleIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['theories'] = TheoryArticleIndexPage.objects.child_of(self).live()
        return context


class StoryArticleIndexPage(TranslationMixin, Page):

    parent_page_types = ['home.HomePage']
    subpage_types = ['articles.StoryArticlePage']

    def get_context(self, request):
        context = super(StoryArticleIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['stories'] = StoryArticleIndexPage.objects.child_of(self).live()
        return context


class AbstractArticle(models.Model):

    subtitle = models.CharField(
        verbose_name=_('subtitle'),
        max_length=255,
        help_text=_("The subtitle of the page"),
        blank=True
    )
    author = models.CharField(
        verbose_name=_('author'),
        max_length=255,
        help_text=_("The author of the article")
    )
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('featured_image'),
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
    publication_date = models.DateField(
        verbose_name=_('publication_date'),
        help_text=_("The publication date of the article"),
        blank=True
    )
    body = RichTextField(
        verbose_name=_('body text'),
        help_text=_("The main text of the article"),
        blank=True
    )

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

StoryArticlePage.content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('author'),
        ImageChooserPanel('featured_image'),
        FieldPanel('summary'),
        FieldPanel('publication_date'),
        FieldPanel('body'),
        InlinePanel('organizations', label=_("Organizations")),
        FieldPanel('tags'),
    ]

StoryArticlePage.promote_panels = Page.promote_panels


class StoryArticlePageOrganization(Orderable, models.Model):
    organization_page =  models.ForeignKey(
        'organizations.OrganizationPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    page = ParentalKey('articles.StoryArticlePage', related_name='organizations')

    panels = [
          PageChooserPanel('organization_page'),
    ]


class TheoryArticlePage(TranslationMixin, Page, AbstractArticle):
    parent_page_types = ['articles.TheoryArticleIndexPage']
    subpage_types = []

    tags = ClusterTaggableManager(through=TheoryArticlePageTag, blank=True)

    class Meta:
        verbose_name = _("Theory")
        verbose_name_plural = _("Theories")

TheoryArticlePage.content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('author'),
        ImageChooserPanel('featured_image'),
        FieldPanel('summary'),
        FieldPanel('publication_date'),
        FieldPanel('body'),
        FieldPanel('tags'),
    ]

TheoryArticlePage.promote_panels = Page.promote_panels


class ReportArticlePage(TranslationMixin, Page, AbstractArticle):
    event_page = models.ForeignKey(
        'events.EventPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    tags = ClusterTaggableManager(through=ReportArticlePageTag, blank=True)

    parent_page_types = ['events.EventPage']
    subpage_types = []

    class Meta:
        verbose_name = _("Event report")

ReportArticlePage.content_panels = Page.content_panels + [
        PageChooserPanel('event_page'),
        FieldPanel('subtitle'),
        FieldPanel('author'),
        ImageChooserPanel('featured_image'),
        FieldPanel('summary'),
        FieldPanel('publication_date'),
        FieldPanel('body'),
        FieldPanel('tags'),
    ]

ReportArticlePage.promote_panels = Page.promote_panels
