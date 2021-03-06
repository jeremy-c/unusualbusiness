from __future__ import unicode_literals  # ensure that RichText.__str__ returns unicode

import re  # parsing HTML with regexes LIKE A BOSS.

from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import escape
from django.utils.safestring import mark_safe

from wagtail.wagtailcore.whitelist import Whitelister
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore import hooks

from django.utils.html import escape
# from wagtailplus.wagtaillinks.rich_text import Link
# from wagtailplus.wagtaillinks.models import Link
from wagtail.wagtaildocs.rich_text import DocumentLinkHandler

from unusualbusiness.articles.models import TheoryArticlePage
from unusualbusiness.definitions.models import DefinitionPage
from unusualbusiness.organizations.models import OrganizationPage

# Define a set of 'embed handlers' and 'link handlers'. These handle the translation
# of 'special' HTML elements in rich text - ones which we do not want to include
# verbatim in the DB representation because they embed information which is stored
# elsewhere in the database and is liable to change - from real HTML representation
# to DB representation and back again.

"""
Contains rich-text link handler definition.
"""


# class UBLinkHandler(object):
#     """
#     LinkHandler will be invoked whenever we encounter an <a> element in HTML content
#     with an attribute of data-linktype="link". The resulting element in the database
#     representation will be: <a linktype="link" id="42">linked text</a>.
#     """
#     @staticmethod
#     def get_db_attributes(tag):
#         """
#         Given an <a> tag that we've identified as a page link embed (because it has a
#         data-linktype="link" attribute), return a dict of the attributes we should
#         have on the resulting <a linktype="link"> element.
#
#         :param tag: the tag dictionary.
#         :rtype: dict.
#         """
#         return {'id': tag['data-id']}
#
#     @staticmethod
#     def expand_db_attributes(attrs, for_editor):
#         """
#         Given a dictionary of attributes, find the corresponding link instance and
#         return its HTML representation.
#
#         :param attrs: dictionary of link attributes.
#         :param for_editor: whether or not HTML is for editor.
#         :rtype: str.
#         """
#         try:
#             editor_attrs    = ''
#             link            = Link.objects.get(id=attrs['id'])
#
#             if for_editor:
#                 editor_attrs = 'data-linktype="link" data-id="{0}" '.format(
#                     link.id
#                 )
#
#             return '<a {0}href="{1}" target="_blank" title="{2}">'.format(
#                 editor_attrs,
#                 escape(link.get_absolute_url()),
#                 link.title
#             )
#         except Link.DoesNotExist:
#             return '<a>'
#
#     @staticmethod
#     def expand_inline_tags(attrs, for_editor):
#         return ''


class UBMarkdownHandler(object):
    """
    UBMarkdownHandler will be invoked whenever we encounter an
    [^123]
    or
    [^123]: string  up to new line.
    element in HTML content.
    The resulting element representation will be:
    <a class="footnote-ref" id="ref-123"></a> or
    <span class="footnote-anchor" id="anchor-123"></span> or
    """

    @staticmethod
    def expand_article_footnote_link_id(id, for_editor):
        if for_editor:
            return ''
        else:
            element_id = "article-footnote-link-{id}".format(id=id)
            element_data_id = "article-footnote-{id}".format(id=id)
            element_classes = 'article-inline-link article-inline-footnote-link'
            return '<a class="{element_classes}" id="{element_id}" data-id="{element_data_id}" href="javascript: void(0)"></a>'.format(
                element_id=element_id,
                element_data_id=element_data_id,
                element_classes=element_classes
            )

    @staticmethod
    def expand_article_footnote_id(id, body, for_editor):
        if for_editor:
            return ''
        else:
            element_id = "article-footnote-{id}".format(id=id)
            element_classes = 'l-body-article-pull-left article-inline article-inline-footnote is-visuallyhidden'
            return '<span class="{element_classes}" id="{element_id}">{body}</span>'.format(
                element_id=element_id,
                element_classes=element_classes,
                body=body
            )

    @staticmethod
    def markdown_to_html_url(body, for_editor):
        if for_editor:
            return ''
        else:
            return FIND_MARKDOWN_URL.sub(replace_url, body)


def replace_url(m):
    url_text = m.group(1)
    url = m.group(2)
    return '<a href="{url}" >{url_text}</a>'.format(
        url_text=url_text,
        url=url
    )


class UBPageLinkHandler(object):
    """
    PageLinkHandler will be invoked whenever we encounter an <a> element in HTML content
    with an attribute of data-linktype="page". The resulting element in the database
    representation will be:
    <a linktype="page" id="42">hello world</a>
    """

    @staticmethod
    def get_db_attributes(tag):
        """
        Given an <a> tag that we've identified as a page link embed (because it has a
        data-linktype="page" attribute), return a dict of the attributes we should
        have on the resulting <a linktype="page"> element.
        """
        return {'id': tag['data-id']}

    @staticmethod
    def expand_db_attributes(attrs, for_editor):
        try:
            page = Page.objects.get(id=attrs['id'])

            if for_editor:
                editor_attrs = 'data-linktype="page" data-id="%d" ' % page.id
            else:
                editor_attrs = ''

            page_type = page.specific._meta.model_name.replace("page", "")

            if isinstance(page.specific, OrganizationPage) \
                or isinstance(page.specific, DefinitionPage) \
                or isinstance(page.specific, TheoryArticlePage):
                return '<a class="article-inline-link article-inline-link-{page_type}" data-id="{page_type}-{id}" {editor_attrs} href="javascript: void(0)">'.format(
                    page_type=page_type,
                    id=page.id,
                    editor_attrs=editor_attrs
                )
            else:
                return '<a class="article-link article-link-{page_type}" {editor_attrs} href="{url}">'.format(
                    page_type=page_type,
                    url=escape(page.url),
                    editor_attrs=editor_attrs
                )

        except Page.DoesNotExist:
            return "<a>"

    @staticmethod
    def expand_inline_tags(attrs, for_editor):
        try:
            page = Page.objects.get(id=attrs['id'])

            if isinstance(page.specific, OrganizationPage):
                return page.specific.render_inline()
            elif isinstance(page.specific, DefinitionPage):
                return page.specific.render_inline()
            elif isinstance(page.specific, TheoryArticlePage):
                return page.specific.render_inline()
            else:
                return ''

        except Page.DoesNotExist:
            return ''


EMBED_HANDLERS = {}
LINK_HANDLERS = {
    'page': UBPageLinkHandler,
    # 'link': UBLinkHandler,
}

# @hooks.register('register_rich_text_link_handler')
# def register_document_link_handler():
#     return ('link', UBLinkHandler)

has_loaded_embed_handlers = False
has_loaded_link_handlers = False


def get_embed_handler(embed_type):
    global EMBED_HANDLERS, has_loaded_embed_handlers

    if not has_loaded_embed_handlers:
        for hook in hooks.get_hooks('register_rich_text_embed_handler'):
            handler_name, handler = hook()
            EMBED_HANDLERS[handler_name] = handler

        has_loaded_embed_handlers = True

    return EMBED_HANDLERS[embed_type]


def get_link_handler(link_type):
    # type: (object) -> object
    # type: (object) -> object
    """

    :rtype: object
    """
    global LINK_HANDLERS, has_loaded_link_handlers

    if not has_loaded_link_handlers:
        for hook in hooks.get_hooks('register_rich_text_link_handler'):
            handler_name, handler = hook()
            LINK_HANDLERS[handler_name] = handler

        has_loaded_link_handlers = True

    return LINK_HANDLERS[link_type]


class DbWhitelister(Whitelister):
    """
    A custom whitelisting engine to convert the HTML as returned by the rich text editor
    into the pseudo-HTML format stored in the database (in which images, documents and other
    linked objects are identified by ID rather than URL):

    * implements a 'construct_whitelister_element_rules' hook so that other apps can modify
      the whitelist ruleset (e.g. to permit additional HTML elements beyond those in the base
      Whitelister module);
    * replaces any element with a 'data-embedtype' attribute with an <embed> element, with
      attributes supplied by the handler for that type as defined in EMBED_HANDLERS;
    * rewrites the attributes of any <a> element with a 'data-linktype' attribute, as
      determined by the handler for that type defined in LINK_HANDLERS, while keeping the
      element content intact.
    """
    has_loaded_custom_whitelist_rules = False

    @classmethod
    def clean(cls, html):
        if not cls.has_loaded_custom_whitelist_rules:
            for fn in hooks.get_hooks('construct_whitelister_element_rules'):
                cls.element_rules = cls.element_rules.copy()
                cls.element_rules.update(fn())
            cls.has_loaded_custom_whitelist_rules = True

        return super(DbWhitelister, cls).clean(html)

    @classmethod
    def clean_tag_node(cls, doc, tag):
        if 'data-embedtype' in tag.attrs:
            embed_type = tag['data-embedtype']
            # fetch the appropriate embed handler for this embedtype
            embed_handler = get_embed_handler(embed_type)
            embed_attrs = embed_handler.get_db_attributes(tag)
            embed_attrs['embedtype'] = embed_type

            embed_tag = doc.new_tag('embed', **embed_attrs)
            embed_tag.can_be_empty_element = True
            tag.replace_with(embed_tag)
        elif tag.name == 'a' and 'data-linktype' in tag.attrs:
            # first, whitelist the contents of this tag
            for child in tag.contents:
                cls.clean_node(doc, child)

            link_type = tag['data-linktype']
            link_handler = get_link_handler(link_type)
            link_attrs = link_handler.get_db_attributes(tag)
            link_attrs['linktype'] = link_type
            tag.attrs.clear()
            tag.attrs.update(**link_attrs)
        else:
            if tag.name == 'div':
                tag.name = 'p'

            super(DbWhitelister, cls).clean_tag_node(doc, tag)


# http://www.regexr.com/
FIND_A_TAG = re.compile(r'<a(\b[^>]*)>')
FIND_ENTIRE_A_TAG = re.compile(r'<a\b[^>]*>([\S\s]*?)<\/a>')
FIND_EMBED_TAG = re.compile(r'<embed(\b[^>]*)/>')
FIND_ATTRS = re.compile(r'([\w-]+)\="([^"]*)"')
FIND_MARKDOWN_NOTE_REF = re.compile(r'\[\^([0-9a-zA-Z])+\]')
FIND_MARKDOWN_NOTE = re.compile(r'\[\^([0-9a-zA-Z]+)\][:](.*?)<\/p>')
FIND_MARKDOWN_URL = re.compile(r'\[([^]]+)]\(\s*(http[s]?://[^)]+)\s*\)')


def extract_attrs(attr_string):
    """
    helper method to extract tag attributes as a dict. Does not escape HTML entities!
    """
    attributes = {}
    for name, val in FIND_ATTRS.findall(attr_string):
        attributes[name] = val
    return attributes


def expand_db_html(html, for_editor=False):
    """
    Expand database-representation HTML into proper HTML usable in either
    templates or the rich text editor
    """

    def replace_a_tag(m):
        attrs = extract_attrs(m.group(1))
        if 'linktype' not in attrs:
            # return unchanged
            return m.group(0)
        handler = get_link_handler(attrs['linktype'])
        return handler.expand_db_attributes(attrs, for_editor)

    def replace_embed_tag(m):
        attrs = extract_attrs(m.group(1))
        handler = get_embed_handler(attrs['embedtype'])
        return handler.expand_db_attributes(attrs, for_editor)

    def add_inline_tag(m):
        found_a_tag = FIND_A_TAG.search(m.string)
        attrs = extract_attrs(found_a_tag.group(1))
        if 'linktype' not in attrs:
            # return unchanged
            return m.group(0)
        handler = get_link_handler(attrs['linktype'])

        # generate inline <span> tag.
        inline_tag = handler.expand_inline_tags(attrs, for_editor)

        # replace <a db-attributes> with real link
        a_tag = FIND_A_TAG.sub(replace_a_tag, m.group(0))

        # add inline <span> tag after <a></a> tag.
        return ''.join([a_tag, inline_tag])

    html = FIND_ENTIRE_A_TAG.sub(add_inline_tag, html)
    html = FIND_EMBED_TAG.sub(replace_embed_tag, html)
    return html


def expand_inline_html(html, for_editor=False):
    """
    Expand database-representation HTML to extra inline HTML elements usable in either
    templates or the rich text editor
    """

    def add_inline_tag(m):
        complete_tag = m.group(0)
        found_a_tag = FIND_A_TAG.search(complete_tag)
        attrs = extract_attrs(found_a_tag.group(1))

        if 'linktype' not in attrs or \
                attrs.get('linktype') == u'document':
            # return unchanged
            return complete_tag
        handler = get_link_handler(attrs['linktype'])

        # generate inline <span> tag.
        inline_tag = handler.expand_inline_tags(attrs, for_editor)
        a_tag = m.group(0)

        # add inline <span> tag after <a></a> tag.
        return ''.join([a_tag, inline_tag])

    def replace_a_tag(m):
        attrs = extract_attrs(m.group(1))
        if 'linktype' not in attrs:
            # return unchanged
            return m.group(0)
        handler = get_link_handler(attrs['linktype'])
        return handler.expand_db_attributes(attrs, for_editor)

    def replace_embed_tag(m):
        attrs = extract_attrs(m.group(1))
        handler = get_embed_handler(attrs['embedtype'])
        return handler.expand_db_attributes(attrs, for_editor)

    def replace_markdown_note_ref(m, for_editor=False):
        footnote_link_id = m.group(0)
        footnote_link_id = footnote_link_id.lstrip('[^')
        footnote_link_id = footnote_link_id.rstrip(']')

        handler = UBMarkdownHandler()
        return handler.expand_article_footnote_link_id(footnote_link_id, for_editor)

    def replace_markdown_note(m, for_editor=False):
        footnote_id = m.group(1)
        footnote_text = m.group(2)
        handler = UBMarkdownHandler()
        footnote_text = handler.markdown_to_html_url(footnote_text, for_editor)
        return handler.expand_article_footnote_id(footnote_id, footnote_text, for_editor)

    html = FIND_ENTIRE_A_TAG.sub(add_inline_tag, html)
    html = FIND_A_TAG.sub(replace_a_tag, html)
    html = FIND_EMBED_TAG.sub(replace_embed_tag, html)
    html = FIND_MARKDOWN_NOTE.sub(replace_markdown_note, html)
    html = FIND_MARKDOWN_NOTE_REF.sub(replace_markdown_note_ref, html)

    return html


@python_2_unicode_compatible
class UBRichText(object):
    """
    A custom object used to represent a renderable rich text value.
    Provides a 'source' property to access the original source code,
    and renders to the front-end HTML rendering.
    Used as the native value of a wagtailcore.blocks.field_block.RichTextBlock.
    """

    def __init__(self, source):
        self.source = (source or '')

    def __str__(self):
        return mark_safe(expand_inline_html(self.source))
