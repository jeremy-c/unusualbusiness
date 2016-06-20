from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from wagtail.wagtailcore.rich_text import RichText
import re

from unusualbusiness.utils.ub_link_handlers import expand_inline_html, UBRichText
from django.utils.text import (slugify as _slugify)
register = template.Library()


@register.filter
def ub_richtext(value):
    if isinstance(value, RichText):
        # passing a RichText value through the |richtext filter should have no effect
        return value
    elif isinstance(value, UBRichText):
        # passing a RichText value through the |richtext filter should have no effect
        return value
    elif value is None:
        html = ''
    else:
        html = expand_inline_html(value)
        # html = expand_db_html(value)

    return mark_safe(html)


@register.filter(is_safe=True)
@stringfilter
def ub_slugify_anchor(value):
    """
    Converts to ASCII. Converts spaces to hyphens. Removes characters that
    aren't alphanumerics, underscores, or hyphens. Converts to lowercase.
    Converts numbers to words. Also strips leading and trailing whitespace.
    """
    replacements = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    return re.sub(r'(\d)', lambda m: replacements.get(m.group(1), m.group(1)), _slugify(value))
