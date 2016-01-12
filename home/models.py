from __future__ import unicode_literals

from itertools import chain

from django.shortcuts import render
from wagtail.wagtailcore.models import Page
from wagtail_modeltranslation.models import TranslationMixin

from articles.models import TheoryArticlePage, ReportArticlePage, StoryArticlePage
from events.models import EventPage
from organizations.models import OrganizationPage


class HomePage(TranslationMixin, Page):
    subpage_types = [
        'articles.StoryArticleIndexPage',
        'articles.TheoryArticleIndexPage',
        'events.EventIndexPage',
        'definitions.DefinitionIndexPage',
        'organizations.OrganizationIndexPage',
        'howtos.HowToIndexPage',
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        # Add extra variables and return the updated context
        context['index_pages'] = Page.objects.child_of(self).live()
        return context

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
