from __future__ import unicode_literals

from django.utils.translation import ugettext as _
from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, TabbedInterface, ObjectList, \
    StreamFieldPanel
from wagtail.wagtailcore.fields import RichTextField, StreamField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail_modeltranslation.models import TranslationMixin
from wagtail.wagtailsearch import index
from wagtail.wagtailcore import blocks


class HomePage(TranslationMixin, Page):
    subpage_types = [
        'articles.StoryArticleIndexPage',
        'articles.TheoryArticleIndexPage',
        'events.EventIndexPage',
        'definitions.DefinitionIndexPage',
        'organizations.OrganizationIndexPage',
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
