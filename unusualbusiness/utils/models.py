from django.db.models import Model
from django.template.loader import get_template
from django.utils.translation import ugettext as _
from wagtail.wagtailcore.models import Page

from unusualbusiness import articles


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

    def related_how_to_theory_articles(self, related_how_tos=None):
        if related_how_tos is None:
            related_how_tos = self.related_how_tos()

        related_how_to_theory_articles = []
        for related_how_to in related_how_tos:
            how_to_articles = related_how_to.theory_pages()
            related_story_articles = self.related_how_to_articles(how_to_articles)
            related_how_to_theory_articles.append({
                related_how_to,
                related_story_articles
            })

        return related_how_to_theory_articles

    def related_how_to_story_articles(self, related_how_tos=None):
        if related_how_tos is None:
            related_how_tos = self.related_how_tos()

        related_how_to_story_articles = []
        for related_how_to in related_how_tos:
            how_to_articles = related_how_to.story_pages()
            related_story_articles = self.related_how_to_articles(how_to_articles)
            related_how_to_story_articles.append({
                related_how_to,
                related_story_articles
            })

        return related_how_to_story_articles

    def related_how_to_articles(self, how_to_articles, self_idx=None):
        previous_article_idx = 0
        next_article_idx = 1

        if self_idx:
            for idx, story in enumerate(how_to_articles):
                if story.id is self_idx:
                    self_idx = idx

            previous_article_idx = self_idx - 1
            next_article_idx = self_idx + 1

        previous_article = None
        next_article = None

        if 0 <= previous_article_idx < len(how_to_articles):
            previous_article = how_to_articles[previous_article_idx]

        if 0 <= next_article_idx < len(how_to_articles):
            next_article = how_to_articles[next_article_idx]

        return (previous_article, next_article)

    def upcoming_related_event_pages(self, related_how_tos=None):
        if related_how_tos is None:
            related_how_tos = self.related_how_tos()

        how_to_events = [how_to_page.events()
                 for how_to_page
                 in related_how_tos]

        event_pages = []
        for how_to_event in how_to_events:
            how_to_event = how_to_event.first()
            if how_to_event and how_to_event.event.is_upcoming:
                event_pages.append(how_to_event.event)

        return event_pages


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
