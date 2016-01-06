from __future__ import unicode_literals
from django.utils.translation import ugettext as _

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, TabbedInterface, ObjectList, \
    StreamFieldPanel
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
    parent_page_types = ['home.HomePage']
    subpage_types = []

    class Meta:
        verbose_name = _("Story")

StoryArticlePage.content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('author'),
        ImageChooserPanel('featured_image'),
        FieldPanel('summary'),
        FieldPanel('publication_date'),
        FieldPanel('body'),
    ]

StoryArticlePage.promote_panels = Page.promote_panels


class TheoryArticlePage(TranslationMixin, Page, AbstractArticle):
    parent_page_types = []
    subpage_types = []

    class Meta:
        verbose_name = _("Theory")

TheoryArticlePage.content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('author'),
        ImageChooserPanel('featured_image'),
        FieldPanel('summary'),
        FieldPanel('publication_date'),
        FieldPanel('body'),
    ]

TheoryArticlePage.promote_panels = Page.promote_panels


class ReportArticlePage(TranslationMixin, Page, AbstractArticle):
    parent_page_types = ['events.EventPage']
    subpage_types = []

    class Meta:
        verbose_name = _("Event report")

ReportArticlePage.content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('author'),
        ImageChooserPanel('featured_image'),
        FieldPanel('summary'),
        FieldPanel('publication_date'),
        FieldPanel('body'),
    ]

ReportArticlePage.promote_panels = Page.promote_panels


class DefinitionPage(TranslationMixin, Page):
    #TODO: add bold and italic to Wysiwyg
    definition = models.TextField(null=True, blank=True)

    parent_page_types = ['articles.DefinitionIndexPage']

    def __str__(self):              # __unicode__ on Python 2
        return self.title

DefinitionPage.content_panels = Page.content_panels + [
        FieldPanel('definition'),
    ]
DefinitionPage.promote_panels = Page.promote_panels


class DefinitionIndexPage(TranslationMixin, Page):

    parent_page_types = ['home.HomePage']
    subpage_types = ['articles.DefinitionPage']

    def get_context(self, request):
        context = super(DefinitionIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['definitions'] = DefinitionPage.objects.child_of(self).live()
        return context