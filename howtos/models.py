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

from articles.models import TheoryArticlePage, StoryArticlePage, ReportArticlePage
from events.models import EventPage
from organizations.models import OrganizationPage
from tags.models import HowToPageTag


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

    def pages(self, tag=None):
        theory_article_page_list = TheoryArticlePage.objects.all().live()
        story_article_page_list = StoryArticlePage.objects.all().live()
        report_article_page_list = ReportArticlePage.objects.all().live()
        event_page_list = EventPage.objects.all().live()
        organization_page_list = OrganizationPage.objects.all().live()

        if tag:
            theory_article_page_list = theory_article_page_list.filter(tags__name=tag)
            story_article_page_list = story_article_page_list.filter(tags__name=tag)
            report_article_page_list = report_article_page_list.filter(tags__name=tag)
            event_page_list = event_page_list.filter(tags__name=tag)
            organization_page_list = organization_page_list.filter(tags__name=tag)

        return sorted(chain(
                theory_article_page_list,
                story_article_page_list,
                report_article_page_list,
                event_page_list,
                organization_page_list
            ),
            key=lambda instance: instance.first_published_at,
            reverse=True)

    def serve(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            pages = self.pages(tag)
        else:
            pages = self.pages()

        return render(request, self.template, {
            'page': self,
            'pages': pages,
        })


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
        return context
