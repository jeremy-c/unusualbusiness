from django import template

from unusualbusiness.articles.models import Quote

register = template.Library()


# Quote snippets
# @register.inclusion_tag('tags/quote.html', takes_context=True)
# def random_quote(context):
#     return {
#         'adverts': Quote.objects.all(),
#         'request': context['request'],
#     }

@register.inclusion_tag('articles/tags/quotes.html', takes_context=True)
def latest_quote(context):
    return {
        'adverts': Quote.objects.first(),
        'request': context['request'],
    }


@register.inclusion_tag('articles/tags/quote.html', takes_context=True)
def all_quotes(context):
    return {
        'adverts': Quote.objects.first(),
        'request': context['request'],
    }
