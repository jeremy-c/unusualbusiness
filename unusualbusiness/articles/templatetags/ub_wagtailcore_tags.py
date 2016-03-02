from django import template
from django.utils.safestring import mark_safe

from articles.ub_page_link_handler import expand_db_html, RichText

register = template.Library()


@register.filter
def ub_richtext(value):
    if isinstance(value, RichText):
        # passing a RichText value through the |richtext filter should have no effect
        return value
    elif value is None:
        html = ''
    else:
        html = expand_db_html(value)

    return mark_safe('<div class="rich-text">' + html + '</div>')
