from __future__ import unicode_literals

from django.db import models
from django.shortcuts import render
from django.template.loader import get_template
from django.template.response import TemplateResponse
from django.utils.translation import ugettext as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail_modeltranslation.models import TranslationMixin

from unusualbusiness.tags.models import OrganizationPageTag
from unusualbusiness.utils.models import RenderInlineMixin, PageFormat


class OrganizationPage(Page, RenderInlineMixin):
    ajax_template = 'organizations/blocks/inline_organization.html'
    format = models.CharField(
        verbose_name=_('page_format'),
        max_length=32,
        null=False,
        default=PageFormat.ORGANIZATION,
        choices=PageFormat.ALL)
    is_featured = models.BooleanField(
        verbose_name = _("Is Featured on home page"),
        default=False
    )
    description = models.CharField(
        verbose_name = _("Description"),
        max_length=512,
        blank=True
    )
    date_founded = models.DateField(
        verbose_name = _("Founded date"),
        null=True,
        blank=True
    )
    amount_of_members = models.PositiveIntegerField(
        verbose_name = _("Amount of members"),
        null=True,
        blank=True
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
    tags = ClusterTaggableManager(through=OrganizationPageTag, blank=True)

    parent_page_types = ['organizations.OrganizationIndexPage']
    subpage_types = []

    search_fields = Page.search_fields + (
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('description_en'),
        index.SearchField('description_nl'),
        index.FilterField('date_founded'),
        index.RelatedFields('story_article_page', [
            index.SearchField('title'),
        ]),
    )

    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('is_featured'),
        FieldPanel('description_en', classname="full"),
        FieldPanel('description_nl', classname="full"),
        FieldPanel('location'),
        FieldPanel('date_founded'),
        FieldPanel('amount_of_members'),
        FieldPanel('email'),
        FieldPanel('website'),
        FieldPanel('facebook'),
        ImageChooserPanel('featured_image'),
        FieldPanel('tags'),
    ]


class OrganizationIndexPage(Page):

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
