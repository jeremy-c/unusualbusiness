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
from unusualbusiness.utils.models import RenderInlineMixin, PageFormat, RelatedHowToMixin


class OrganizationPage(Page, RenderInlineMixin, RelatedHowToMixin):
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
    description = models.TextField(
        verbose_name=_("Description"),
        max_length=1024,
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
    address = models.CharField(
        verbose_name=_("Address"),
        max_length=128,
        blank=True
    )
    postal_code = models.CharField(
        verbose_name=_("Postal code"),
        max_length=8,
        blank=True
    )
    city = models.CharField(
        verbose_name=_("City"),
        max_length=64,
        blank=True
    )
    country = models.CharField(
        verbose_name=_("Country"),
        max_length=64,
        blank=True
    )
    email = models.EmailField(
        verbose_name=_("Email"),
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
    twitter = models.URLField(
        verbose_name = _("Twitter"),
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

    class Meta:
        verbose_name = _("Practitioner")
        verbose_name_plural = _("Practitioners")

    def related_story_articles(self):
        return [related_story_article_page.story_article_page
                    for related_story_article_page
                    in self.story_article_page.select_related().all()]

    def location(self):
        return ", ".join([self.address,
                        self.postal_code,
                        self.city,
                        self.country
                        ])

    def get_context(self, request):
        context = super(OrganizationPage, self).get_context(request)

        related_how_tos = self.related_how_tos()

        context['related_how_tos'] = related_how_tos
        context['upcoming_related_event'] = self.upcoming_related_event(related_how_tos)
        context['related_story_articles'] = self.related_story_articles()

        return context

    parent_page_types = ['organizations.OrganizationIndexPage']
    subpage_types = []

    search_fields = Page.search_fields + [
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('description_en'),
        index.SearchField('description_nl'),
        index.FilterField('date_founded'),
        index.FilterField('city'),
        index.FilterField('country'),
        index.RelatedFields('story_article_page', [
            index.SearchField('title'),
        ]),
    ]

    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('is_featured'),
        FieldPanel('description_en', classname="full"),
        FieldPanel('description_nl', classname="full"),
        FieldPanel('address'),
        FieldPanel('postal_code'),
        FieldPanel('city'),
        FieldPanel('country'),
        FieldPanel('date_founded'),
        FieldPanel('amount_of_members'),
        FieldPanel('email'),
        FieldPanel('website'),
        FieldPanel('facebook'),
        FieldPanel('twitter'),
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

    class Meta:
        verbose_name = _("Practitioner")
        verbose_name_plural = _("Practitioners")

    def get_context(self, request):
        context = super(OrganizationIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['articles'] = OrganizationPage.objects.child_of(self).live().order_by('title')
        return context
