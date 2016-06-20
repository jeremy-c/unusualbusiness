from __future__ import unicode_literals
from django.db import models
from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import ugettext as _
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, PageChooserPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from unusualbusiness.events.models import EventPage
from unusualbusiness.organizations.models import OrganizationPage


class HowToPage(Page):
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

    search_fields = Page.search_fields + [
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
        index.RelatedFields('news_article_pages', [
            index.SearchField('title'),
        ]),
        index.RelatedFields('event_pages', [
            index.SearchField('title'),
        ]),
    ]

    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('description_en', classname="full"),
        FieldPanel('description_nl', classname="full"),
        ImageChooserPanel('featured_image'),
        InlinePanel('organization_pages', label=_("Organizations")),
        InlinePanel('story_article_pages', label=_("Story Articles")),
        InlinePanel('theory_article_pages', label=_("Theory Articles")),
        InlinePanel('news_article_pages', label=_("News Articles")),
        InlinePanel('event_pages', label=_("Events")),
    ]

    # Parent page / subpage type rules]
    parent_page_types = ['howtos.HowToIndexPage']
    subpage_types = []

    class Meta:
        verbose_name = _("How to")
        verbose_name_plural = _("How to's")

    def theory_page_list(self):
        theory_page_list = []
        theory_article_pages = self.theory_article_pages.all()

        for theory_article_page in theory_article_pages:
            theory_page_list.append(theory_article_page.article)

        return theory_page_list

    def story_page_list(self):
        story_pages = []
        story_article_pages = self.story_article_pages.all()

        for story_article_page in story_article_pages:
            story_pages.append(story_article_page.article)

        return story_pages

    def news_page_list(self):
        news_pages = []
        news_article_pages = self.news_article_pages.all()

        for news_article_page in news_article_pages:
            news_pages.append(news_article_page.article)

        return news_pages

    def organizations(self):
        organization_pages = self.organization_pages.all()

        return organization_pages

    def organization_list(self):
        organization_pages = self.organization_pages.all()
        organization_list = []

        for organization_page in organization_pages:
            organization_list.append(organization_page.organization)

        return organization_list

    def event_page_list(self):
        event_pages = []
        event_pages_qs = self.event_pages.all()

        for event_page_qs in event_pages_qs.all():
            event_pages.append(event_page_qs.event)

        return event_pages

    def upcoming_events(self):
        now = timezone.now().date()
        return [event_page.event for event_page in self.event_pages.all() if event_page.event.start_date.date() >= now]

    def circles(self):
        circles = ''

        if self.organizations().count() > 0:
            circles += 'practitioners'
        if len(self.story_page_list()) > 0:
            circles += ' stories'
        if len(self.theory_page_list()) > 0:
            circles += ' theory'
        if len(self.event_page_list()) > 0 or len(self.news_page_list()) > 0:
            circles += ' activities'
        if len(self.upcoming_events()) > 0:
            circles += ' upcoming-event'

        return circles

    def page_formats(self):
        news_text_count = 0
        news_video_count = 0
        news_images_count = 0
        news_audio_count = 0
        story_text_count = 0
        story_video_count = 0
        story_images_count = 0
        story_audio_count = 0
        theory_count = len(self.theory_page_list())
        organization_count = self.organizations().count()
        link_count = 0

        story_article_pages = self.story_article_pages.all()
        for story_article_page in story_article_pages:
            if story_article_page.article.format == 'text':
                story_text_count += 1
            elif story_article_page.article.format == 'video':
                story_video_count += 1
            elif story_article_page.article.format == 'images':
                story_images_count += 1
            elif story_article_page.article.format == 'audio':
                story_audio_count += 1

        news_article_pages = self.news_article_pages.all()
        for news_article_page in news_article_pages:
            if news_article_page.article.format == 'text':
                news_text_count += 1
            elif news_article_page.article.format == 'video':
                news_video_count += 1
            elif news_article_page.article.format == 'images':
                news_images_count += 1
            elif news_article_page.article.format == 'audio':
                news_audio_count += 1

        return [{
                'page_type': 'theory',
                'page_format': 'theory',
                'page_count': theory_count
             },{
                'page_type': 'activities',
                'page_format': 'text',
                'page_count': news_text_count
             }, {
                'page_type': 'activities',
                'page_format': 'video',
                'page_count': news_video_count
             },{
                'page_type': 'theory',
                'page_format': 'link',
                'page_count': link_count
             }, {
                'page_type': 'activities',
                'page_format': 'audio',
                'page_count': news_audio_count
             }, {
                'page_type': 'stories',
                'page_format': 'text',
                'page_count': story_text_count
             }, {
                'page_type': 'practitioners',
                'page_format': 'organization',
                'page_count': organization_count
             }, {
                'page_type': 'stories',
                'page_format': 'video',
                'page_count': story_video_count
             }, {
                'page_type': 'activities',
                'page_format': 'images',
                'page_count': news_images_count
             }, {
                'page_type': 'stories',
                'page_format': 'images',
                'page_count': story_images_count
             }, {
                'page_type': 'stories',
                'page_format': 'audio',
                'page_count': story_audio_count
             },
        ]

    def serve(self, request):
        theory_pages = self.theory_page_list()
        story_pages = self.story_page_list()
        news_pages = self.news_page_list()
        organizations = self.organization_list()
        events = self.event_page_list()

        upcoming_related_event = None
        if len(self.upcoming_events()) > 0:
            upcoming_related_event = self.upcoming_events()[0]

        return render(request, self.template, {
            'self': self,
            'theory_articles': theory_pages,
            'story_articles': story_pages,
            'news_articles': news_pages,
            'organizations': organizations,
            'event_pages': events,
            'page_formats': self.page_formats(),
            'upcoming_related_event': upcoming_related_event
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


class HowToPageNewsArticlePage(Orderable, models.Model):
    how_to_page = ParentalKey('howtos.HowToPage', related_name='news_article_pages')
    article = models.ForeignKey(
        'articles.NewsArticlePage',
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


class HowToIndexPage(Page):
    parent_page_types = ['pages.HomePage']
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
