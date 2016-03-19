from __future__ import unicode_literals
from itertools import chain

from django.db import models
from django.shortcuts import render
from django.utils.translation import ugettext as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, PageChooserPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail_modeltranslation.models import TranslationMixin

from unusualbusiness.articles.models import TheoryArticlePage, StoryArticlePage, ReportArticlePage
from unusualbusiness.events.models import EventPage
from unusualbusiness.organizations.models import OrganizationPage
from unusualbusiness.tags.models import HowToPageTag


class HowToPage(TranslationMixin, Page):
    description = RichTextField(
        verbose_name = _("Description"),
        null=True
    )
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name = _("Featured image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    tags = ClusterTaggableManager(through=HowToPageTag, blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('description_en'),
        index.SearchField('description_nl'),

        index.RelatedFields('story_article_pages', [
            index.SearchField('title'),
        ]),
        index.RelatedFields('theory_article_pages', [
            index.SearchField('title'),
        ]),
        index.RelatedFields('event_pages', [
            index.SearchField('title'),
        ]),
    )

    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('description_en', classname="full"),
        FieldPanel('description_nl', classname="full"),
        ImageChooserPanel('featured_image'),
        InlinePanel('organization_pages', label=_("Organizations")),
        InlinePanel('story_article_pages', label=_("Story Articles")),
        InlinePanel('theory_article_pages', label=_("Theory Articles")),
        InlinePanel('event_pages', label=_("Events")),
        FieldPanel('tags'),
    ]

    # Parent page / subpage type rules]
    parent_page_types = ['howtos.HowToIndexPage']
    subpage_types = []

    class Meta:
        verbose_name = _("How to")
        verbose_name_plural = _("How to's")

    def theory_pages(self, tag=None):
        theory_article_pages= self.theory_article_pages.all()

        if tag:
            theory_article_pages = theory_article_pages.filter(tags__name=tag)

        return theory_article_pages

    def story_pages(self, tag=None):
        story_article_pages = self.story_article_pages.all()

        if tag:
            story_article_pages = story_article_pages.filter(tags__name=tag)

        return story_article_pages

    def organizations(self, tag=None):
        organization_pages = self.organization_pages.all()

        if tag:
            organization_pages = organization_pages.filter(tags__name=tag)

        return organization_pages

    def serve(self, request):
        tag = request.GET.get('tag')
        if tag:
            theory_pages = self.theory_pages(tag)
            story_pages = self.story_pages(tag)
            organization_pages = self.organizations(tag)
            theory_pages = self.theory_pages(tag)
        else:
            theory_pages = self.theory_pages()
            story_pages = self.story_pages()
            organization_pages = self.organizations()
            theory_pages = self.theory_pages()

        return render(request, self.template, {
            'self': self,
            'theory_pages': theory_pages,
            'story_pages': story_pages,
            'organization_pages': organization_pages,
        })


class HowToPageOrganizationPage(Orderable, models.Model):
    how_to_page = ParentalKey('howtos.HowToPage', related_name='organization_pages')
    organization = models.ForeignKey(
        'organizations.OrganizationPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='how_to_page'
    )

    panels = [
      PageChooserPanel('organization'),
    ]

    def __str__(self):              # __unicode__ on Python 2
        return self.how_to_page.title + " -> " + self.organization.title


class HowToPageStoryArticlePage(Orderable, models.Model):
    how_to_page = ParentalKey('howtos.HowToPage', related_name='story_article_pages')
    article = models.ForeignKey(
        'articles.StoryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='how_to_page'
    )

    panels = [
      PageChooserPanel('article'),
    ]

    def __str__(self):              # __unicode__ on Python 2
        return self.how_to_page.title + " -> " + self.article.title


class HowToPageTheoryArticlePage(Orderable, models.Model):
    how_to_page = ParentalKey('howtos.HowToPage', related_name='theory_article_pages')
    article = models.ForeignKey(
        'articles.TheoryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='how_to_page'
    )

    panels = [
      PageChooserPanel('article'),
    ]

    def __str__(self):              # __unicode__ on Python 2
        return self.how_to_page.title + " -> " + self.article.title


class HowToPageEventPage(Orderable, models.Model):
    how_to_page = ParentalKey('howtos.HowToPage', related_name='event_pages')
    event = models.ForeignKey(
        'events.EventPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='how_to_page'
    )

    panels = [
      PageChooserPanel('event'),
    ]

    def __str__(self):              # __unicode__ on Python 2
        return self.how_to_page.title + " -> " + self.event.title


class HowToIndexPage(TranslationMixin, Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['howtos.HowToPage']

    class Meta:
        verbose_name = _("How to Index Page")
        verbose_name_plural = _("How to Index Pages")

    def get_context(self, request):
        context = super(HowToIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['how_tos'] = HowToPage.objects.child_of(self).live()
        context['parent'] = self.get_parent()
        context['upcoming_events'] = EventPage.upcoming_events()
        return context

