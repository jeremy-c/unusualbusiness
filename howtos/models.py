from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, PageChooserPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail_modeltranslation.models import TranslationMixin

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


class HowToPageStoryArticlePage(Orderable, models.Model):
    how_to_page = ParentalKey('howtos.HowToPage', related_name='story_article_pages')
    article = models.ForeignKey(
        'articles.StoryArticlePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
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
        related_name='+'
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
        related_name='+'
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
