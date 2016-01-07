from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from taggit.managers import TaggableManager
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

from articles.models import TaggedPage


class OrganizationPage(TranslationMixin, Page):

    description = RichTextField(
        verbose_name = _("Description"),
        null=True
    )
    date_founded = models.DateField(
        verbose_name = _("Founded date"),
        null=True,
        blank=True
    )
    amount_of_members = models.PositiveIntegerField(
        verbose_name = _("Amount of members"),
        null=True
    )
    # This should probably be a specific geolocation field:
    location = models.CharField(
        verbose_name = _("Location"),
        max_length=512,
        blank=True
    )
    email = models.EmailField(
        verbose_name = _("Email"),
        blank=True
    )
    website = models.URLField(
        verbose_name = _("Website"),
        blank=True
    )
    facebook = models.URLField(
        verbose_name = _("Facebook"),
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
    tags = TaggableManager(through=TaggedPage, blank=True)

    # Search index configuration

    search_fields = Page.search_fields + (
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('description_en'),
        index.SearchField('description_nl'),
        index.FilterField('date_founded'),
    )

    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('date_founded'),
        FieldPanel('description_en', classname="full"),
        FieldPanel('description_nl', classname="full"),
        FieldPanel('location'),
        FieldPanel('email'),
        FieldPanel('website'),
        FieldPanel('facebook'),
        ImageChooserPanel('featured_image'),
        FieldPanel('tags'),
    ]

    # Parent page / subpage type rules]
    parent_page_types = ['organizations.OrganizationIndexPage']
    subpage_types = []


class OrganizationIndexPage(TranslationMixin, Page):

    # content_panels = Page.content_panels + [
    # ]
    #
    # dutch_content_panels = [
    #     FieldPanel('title_nl', classname="full"),
    # ]
    #
    # promote_panels = [
    #     MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    #     FieldPanel('slug_nl'),
    # ]
    #
    # edit_handler = TabbedInterface([
    #     ObjectList(content_panels, heading='English'),
    #     ObjectList(dutch_content_panels, heading='Nederlands'),
    #     ObjectList(Page.promote_panels, heading='Promote'),
    #     ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    # ])

    parent_page_types = ['home.HomePage']
    subpage_types = ['organizations.OrganizationPage']

    def get_context(self, request):
        context = super(OrganizationIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['organizations'] = OrganizationPage.objects.child_of(self).live()
        return context
