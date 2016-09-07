from django import template

from unusualbusiness.pages.models import Quote, StaticContent

register = template.Library()


@register.inclusion_tag('pages/blocks/quote.html', takes_context=True)
def latest_quote(context):
    return {
        'quote': Quote.objects.first(),
        'request': context['request'],
    }


@register.inclusion_tag('pages/blocks/quote.html', takes_context=True)
def second_quote(context):
    quotes = Quote.objects.all()
    quote = None
    if quotes.count() > 1:
        quote = quotes[1]
    return {
        'quote': quote,
        'request': context['request'],
    }


@register.inclusion_tag('pages/blocks/quotes.html', takes_context=True)
def all_quotes(context):
    return {
        'quotes': Quote.objects.all(),
        'request': context['request'],
    }


@register.inclusion_tag('pages/blocks/static_content.html', takes_context=True)
def static_content(context):
    return {
        'static_content': StaticContent.objects.select_related('page'),
        'request': context['request'],
    }
