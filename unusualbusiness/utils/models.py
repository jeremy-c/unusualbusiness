from django.db.models import Model, CharField
from django.template.loader import get_template
from django.utils.translation import ugettext as _
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore import blocks
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsnippets.models import register_snippet

# Blocks

class Heading2Block(blocks.StructBlock):
    chapter_name = \
        blocks.CharBlock(required=True)

    class Meta:
        template = 'articles/blocks/heading2.html'
        icon = 'title'
        label = _('Chapter (h2)')


class Heading3Block(blocks.StructBlock):
    section_name = blocks.CharBlock(required=True)

    class Meta:
        template = 'articles/blocks/heading3.html'
        icon = 'title'
        label = _('Section (h3)')


class Heading4Block(blocks.StructBlock):
    subsection_name = blocks.CharBlock(required=True)

    class Meta:
        template = 'articles/blocks/heading4.html'
        icon = 'title'
        label = _('Subsection (h4)')


class PullQuoteBlock(blocks.StructBlock):
    pull_quote = blocks.CharBlock(required=True)

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
        # related_how_to_qs = self.how_to_page.select_related().all()
        #
        # related_how_tos = []
        # for related_how_to in related_how_to_qs.how_to_page:
        #     related_how_tos.append(related_how_to.how_to_page)
        #
        # return related_how_tos

    def related_how_to_theory_articles(self, related_how_tos=None, self_idx=None):
        if related_how_tos is None:
            related_how_tos = self.related_how_tos()

        related_how_to_theory_articles = []
        for related_how_to in related_how_tos:
            how_to_articles = related_how_to.theory_pages()
            related_story_articles = self.related_how_to_pages(how_to_articles, self_idx)
            related_how_to_theory_articles.append({
                related_how_to,
                related_story_articles
            })

        return related_how_to_theory_articles

    def related_how_to_story_articles(self, related_how_tos=None, self_idx=None):
        if related_how_tos is None:
            related_how_tos = self.related_how_tos()

        related_how_to_story_articles = []
        for related_how_to in related_how_tos:
            how_to_articles = related_how_to.story_pages()
            related_story_articles = self.related_how_to_pages(how_to_articles, self_idx)
            related_how_to_story_articles.append({
                related_how_to,
                related_story_articles
            })

        return related_how_to_story_articles

    def related_how_to_news_articles(self, related_how_tos=None, self_idx=None):
        if related_how_tos is None:
            related_how_tos = self.related_how_tos()

        related_how_to_news_articles = []
        for related_how_to in related_how_tos:
            how_to_articles = related_how_to.news_pages()
            related_news_articles = self.related_how_to_pages(how_to_articles, self_idx)
            related_how_to_news_articles.append({
                'how_to': related_how_to,
                'articles': related_news_articles
            })

        return related_how_to_news_articles

    def related_how_to_events(self, related_how_tos=None, self_idx=None):
        if related_how_tos is None:
            related_how_tos = self.related_how_tos()

        related_how_to_events = []
        for related_how_to in related_how_tos:
            how_to_events = related_how_to.events()
            related_events = self.related_how_to_pages(how_to_events, self_idx)
            related_how_to_events.append(related_events)

        return related_how_to_events

    def upcoming_related_event(self, related_how_tos=None):
        if related_how_tos is None:
            related_how_tos = self.related_how_tos()

        how_to_event_lists = [how_to_page.events()
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


class PageFormat:
    EVENT = 'event'
    VIDEO = 'video'
    TEXT = 'text'
    IMAGES = 'images'
    AUDIO = 'audio',
    ORGANIZATION = 'organization'
    THEORY = 'theory'
    LINK = 'link'
    DOCUMENT = 'document'

    ALL = (
        (TEXT, _('Normal Article')),
        (THEORY, _('Theory Article')),
        (VIDEO, _('Video embed')),
        (AUDIO, _('Audio embed')),
        (IMAGES, _('Image slideshow')),
        (EVENT, _('Event')),
        (ORGANIZATION, _('Organization')),
        (LINK, _('External Link')),
        (DOCUMENT, _('Document Download')),
    )

    def __init__(self):
        pass

