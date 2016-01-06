from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
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


class EventPage(TranslationMixin, Page):

    start_date = models.DateField(
        verbose_name = _("Starting date"),
        null=True
    )
    start_time = models.TimeField(
        verbose_name = _("Starting time")
    )
    end_date = models.DateField(
        verbose_name = _("End date"),
        null=True
    )
    end_time = models.TimeField(
        verbose_name = _("End time")
    )
    # This should probably be a specific geolocation field:
    location = models.CharField(
        verbose_name = _("Location"),
        max_length=512,
        blank=True
    )
    # TODO: Add participating groups as ForeignKeys
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
    poster_link = models.URLField(
        verbose_name = _("Poster"),
        blank=True
    )
    flyer_link = models.URLField(
        verbose_name = _("Flyer"),
        blank=True
    )
    facebook_event = models.URLField(
        verbose_name = _("Facebook event"),
        blank=True
    )

class EventIndexPage(TranslationMixin, Page):

    subpage_types = ['events.EventPage']

    def get_context(self, request):
        context = super(EventIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['events'] = EventPage.objects.child_of(self).live()
        return context