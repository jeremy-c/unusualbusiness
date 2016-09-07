from django.db.models import Model, CharField, URLField
from django.template.loader import get_template
from django.utils.translation import ugettext as _
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore import blocks
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from wagtail.wagtailcore import hooks
from wagtail.wagtailcore.whitelist import attribute_rule, check_url, allow_without_attributes


class RenderInlineMixin(object):
    def __init__(self):
        pass

    def render_inline(self):
        template = get_template(self.ajax_template)
        return template.render({
            'self': self
        })


class RelatedHowToMixin(object):
    def __init__(self):
        pass

    def related_how_tos(self):
        return [related_how_to_page.how_to_page
                   for related_how_to_page
                   in self.how_to_page.select_related().all()]

    def related_how_to_theory_articles(self, related_how_tos=None, self_idx=None):
        if related_how_tos is None:
            related_how_tos = self.related_how_tos()

        related_how_to_theory_articles = []
        for related_how_to in related_how_tos:
            how_to_articles = related_how_to.theory_page_list()
            related_articles = self.related_how_to_pages(how_to_articles, self_idx)
            related_how_to_theory_articles.append({
                'how_to': related_how_to,
                'articles': related_articles
            })

        return related_how_to_theory_articles

    def related_how_to_story_articles(self, related_how_tos=None, self_idx=None):
        if related_how_tos is None:
            related_how_tos = self.related_how_tos()

        related_how_to_story_articles = []
        for related_how_to in related_how_tos:
            how_to_articles = related_how_to.story_page_list()
            related_articles = self.related_how_to_pages(how_to_articles, self_idx)
            related_how_to_story_articles.append({
                'how_to': related_how_to,
                'articles': related_articles
            })

        return related_how_to_story_articles

    def related_how_to_news_articles(self, related_how_tos=None, self_idx=None):
        if related_how_tos is None:
            related_how_tos = self.related_how_tos()

        related_how_to_news_articles = []
        for related_how_to in related_how_tos:
            how_to_articles = related_how_to.news_page_list()
            related_articles = self.related_how_to_pages(how_to_articles, self_idx)
            related_how_to_news_articles.append({
                'how_to': related_how_to,
                'articles': related_articles
            })

        return related_how_to_news_articles

    def related_how_to_events(self, related_how_tos=None, self_idx=None):
        if related_how_tos is None:
            related_how_tos = self.related_how_tos()

        related_how_to_events = []
        for related_how_to in related_how_tos:
            how_to_events = related_how_to.event_page_list()
            related_events = self.related_how_to_pages(how_to_events, self_idx)
            related_how_to_events.append(related_events)

        return related_how_to_events

    def upcoming_related_event(self, related_how_tos=None):
        if related_how_tos is None:
            related_how_tos = self.related_how_tos()

        how_to_event_lists = [how_to_page.event_page_list()
             for how_to_page
             in related_how_tos]

        event_pages = []
        for how_to_event_list in how_to_event_lists:
            if len(how_to_event_list) > 0:
                for how_to_event in how_to_event_list:
                    if how_to_event and how_to_event.is_upcoming:
                        event_pages.append(how_to_event)

        if len(event_pages) > 0:
            return sorted(event_pages, key=lambda event: event.start_date)[0]
        return event_pages

    @staticmethod
    def related_how_to_pages(how_to_pages, self_idx=None):
        previous_page_idx = 0
        next_article_idx = 1

        if self_idx:
            for idx, page in enumerate(how_to_pages):
                if page.id is self_idx:
                    self_idx = idx

            previous_page_idx = self_idx - 1
            next_article_idx = self_idx + 1

        previous_page = None
        next_page = None

        if 0 <= previous_page_idx < len(how_to_pages):
            previous_page = how_to_pages[previous_page_idx]

        if 0 <= next_article_idx < len(how_to_pages):
            next_page = how_to_pages[next_article_idx]

        return (previous_page, next_page)


# Blocks


class PullQuoteBlock(blocks.StructBlock):
    pull_quote = blocks.TextBlock(verbose_name=_('Pull quote'),
                                  required=True,
                                  rows=2)
    attribution = blocks.CharBlock(verbose_name=_('Quote attribution to'),
                                   help_text=_('The name of the person or organization that '
                                               'the quote can be attributed to quote'),
                                   required=False)
    link = blocks.URLBlock(verbose_name=_('Link'),
                           help_text=_("Click quote to go to link."),
                           required=False)

    class Meta:
        template = 'articles/blocks/pullquote.html'
        icon = 'openquote'
        label = 'Pull Quote'


class FeaturedImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)

    class Meta:
        icon='image'
        label=_('Image')
        template='articles/blocks/featured_image.html'
        help_text=_('The featured image is shown in the list-view and detail-view')


class FeaturedVideoBlock(blocks.StructBlock):
    video = EmbedBlock(required=True)

    class Meta:
        icon='media'
        label=_('Video')
        template='articles/blocks/featured_video.html'
        help_text=_('The featured video is only shown in the detail-view, make sure to also selecte a featured image')


class FeaturedAudioBlock(blocks.StructBlock):
    audio = EmbedBlock(required=True)

    class Meta:
        icon='media'
        label=_('Audio')
        template='articles/blocks/featured_audio.html'
        help_text=_('The featured audio is only shown in the detail-view, make sure to also selecte a featured image')


class PageFormat:
    TEXT = ('text', _('Story'))
    THEORY = ('theory', _('Theory'))
    VIDEO = ('video', _('Video'))
    AUDIO = ('audio', _('Audio'))
    IMAGES = ('images', _('Photo report'))
    EVENT = ('event', _('Activity'))
    ORGANIZATION = ('organization', _('Practitioner'))
    LINK = ('link', _('Link'))
    DOCUMENT = ('document', _('Document'))

    ALL = (
        TEXT,
        THEORY,
        VIDEO,
        AUDIO,
        IMAGES,
        EVENT,
        ORGANIZATION,
        LINK,
        DOCUMENT
    )

    def __init__(self):
        pass
