from django import template
from django.utils.safestring import mark_safe
from wagtail.wagtailcore.rich_text import RichText

from unusualbusiness.utils.ub_link_handlers import expand_inline_html, UBRichText

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
