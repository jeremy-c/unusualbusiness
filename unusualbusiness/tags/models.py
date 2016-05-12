from __future__ import unicode_literals

from modelcluster.fields import ParentalKey
from taggit.models import CommonGenericTaggedItemBase, TaggedItemBase, TagBase, GenericTaggedItemBase, ItemBase
from wagtail.wagtailcore.models import Page


class HowToPageTag(TaggedItemBase):
    content_object = ParentalKey('howtos.HowToPage', related_name='tagged_items')


class EventPageTag(TaggedItemBase):
    content_object = ParentalKey('events.EventPage', related_name='tagged_items')


class TheoryArticlePageTag(TaggedItemBase):
    content_object = ParentalKey('articles.TheoryArticlePage', related_name='tagged_items')


class StoryArticlePageTag(TaggedItemBase):
    content_object = ParentalKey('articles.StoryArticlePage', related_name='tagged_items')


class NewsArticlePageTag(TaggedItemBase):
    content_object = ParentalKey('articles.NewsArticlePage', related_name='tagged_items')


class OrganizationPageTag(TaggedItemBase):
    content_object = ParentalKey('organizations.OrganizationPage', related_name='tagged_items')

