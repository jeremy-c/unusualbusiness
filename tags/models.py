from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from taggit.models import CommonGenericTaggedItemBase, TaggedItemBase, TagBase, GenericTaggedItemBase
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page


class EventPageTag(TaggedItemBase):
    content_object = ParentalKey('events.EventPage', related_name='tagged_items')


class TheoryArticlePageTag(TaggedItemBase):
    content_object = ParentalKey('articles.TheoryArticlePage', related_name='tagged_items')


class StoryArticlePageTag(TaggedItemBase):
    content_object = ParentalKey('articles.StoryArticlePage', related_name='tagged_items')


class ReportArticlePageTag(TaggedItemBase):
    content_object = ParentalKey('articles.ReportArticlePage', related_name='tagged_items')


class OrganizationPageTag(TaggedItemBase):
    content_object = ParentalKey('organizations.OrganizationPage', related_name='tagged_items')