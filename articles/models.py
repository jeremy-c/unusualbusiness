from __future__ import unicode_literals
from django.utils.translation import ugettext as _

from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, TabbedInterface, ObjectList, \
    StreamFieldPanel
from wagtail.wagtailcore.fields import RichTextField, StreamField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail_modeltranslation.models import TranslationMixin
from wagtail.wagtailsearch import index
from wagtail.wagtailcore import blocks


class ArticlePage(TranslationMixin, Page):

    # Database fields

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

    # Search index configuraiton

    search_fields = Page.search_fields + (
        index.SearchField('title'),
        index.SearchField('subtitle'),
        index.SearchField('author'),
        index.SearchField('summary'),
        index.SearchField('body'),
    )

    # Parent page / subpage type rules]
    parent_page_types = ['articles.ArticlePage']
    subpage_types = ['articles.ArticlePage']