from __future__ import unicode_literals

from itertools import chain

from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from django.db import models
from django.db.models import Model, URLField
from django.shortcuts import render
from modelcluster.fields import ParentalKey
from taggit.models import Tag
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailcore.models import Page
from django.utils.translation import ugettext as _
from wagtail.wagtailsnippets.models import register_snippet

from unusualbusiness.articles.models import TheoryArticlePage, NewsArticlePage, StoryArticlePage
from unusualbusiness.events.models import EventPage
from unusualbusiness.howtos.models import HowToPage
from unusualbusiness.organizations.models import OrganizationPage
from wagtail.wagtailcore.models import Page, Orderable


class HomePage(Page):
    subpage_types = [
        'articles.StoryArticleIndexPage',
        'articles.TheoryArticleIndexPage',
        'articles.ActivityIndexPage',
        'articles.AuthorIndexPage',
        'definitions.DefinitionIndexPage',
        'organizations.OrganizationIndexPage',
        'howtos.HowToIndexPage',
        'pages.GeneralPage',
    ]

    def how_tos(self):
        return HowToPage.objects.all().live()

    def tags(self):
        return Tag.objects.all()

    def pages(self, tag=None):
        theory_article_page_list = TheoryArticlePage.objects.all().live()
        story_article_page_list = StoryArticlePage.objects.all().live()
        news_article_page_list = NewsArticlePage.objects.all().live()
        event_page_list = EventPage.objects.all().live()
        organization_page_list = OrganizationPage.objects.all().live()

        if tag:
            theory_article_page_list = theory_article_page_list.filter(tags__name=tag)
            story_article_page_list = story_article_page_list.filter(tags__name=tag)
            news_article_page_list = news_article_page_list.filter(tags__name=tag)
            event_page_list = event_page_list.filter(tags__name=tag)
            organization_page_list = organization_page_list.filter(tags__name=tag)

        return sorted(chain(
                theory_article_page_list,
                story_article_page_list,
                news_article_page_list,
                event_page_list,
                organization_page_list
            ),
            key=lambda instance: instance.first_published_at,
            reverse=True)

    @staticmethod
    def featured_articles():
        theory_article_list = TheoryArticlePage.objects.live().filter(is_featured=True)
        story_article_list = StoryArticlePage.objects.live().filter(is_featured=True)
        news_article_list = NewsArticlePage.objects.live().filter(is_featured=True)
        event_list = EventPage.objects.live().filter(is_featured=True)

        return sorted(chain(
            theory_article_list,
            story_article_list,
            news_article_list,
            event_list
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

        how_tos = self.how_tos()

        return render(request, self.template, {
            'page': self,
            'articles': pages,
            'featured_articles': self.featured_articles(),
            'upcoming_events': EventPage.upcoming_events(),
            'how_tos': how_tos,
            'tags': self.tags,
        })

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        # Add extra variables and return the updated context
        # context['index_pages'] = Page.objects.child_of(self).live()
        return context

    content_panels = Page.content_panels + [
        InlinePanel('static_content_placements', label="Static Content"),
    ]

            # dutch_content_panels = [
    #     FieldPanel('title_nl', classname="full"),
    #     FieldPanel('body_nl', classname="full"),
    #     StreamFieldPanel('stream_nl'),
    # ]
    #
    # promote_panels = Page.promote_panels + [
    #     ImageChooserPanel('feed_image'),
    #     FieldPanel('date'),
    # ]
    #
    # edit_handler = TabbedInterface([
    #     ObjectList(content_panels, heading='English'),
    #     ObjectList(dutch_content_panels, heading='Nederlands'),
    #     ObjectList(Page.promote_panels, heading='Promote'),
    #     ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    # ])

    # Parent page / subpage type rules


class HomePageStaticContentPlacement(Orderable, Model):
    home_page = ParentalKey('home.HomePage', related_name='static_content_placements')
    static_content = models.ForeignKey('pages.StaticContent', related_name='+')

    class Meta:
        verbose_name = "Static content placement"
        verbose_name_plural = "Static content placements"

    panels = [
        SnippetChooserPanel('static_content'),
    ]

    def __str__(self):              # __unicode__ on Python 2
        return self.home_page.title + " -> " + self.static_content.body
