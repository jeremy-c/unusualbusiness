from django import template

register = template.Library()


@register.simple_tag
def get_verbose_name_plural(queryset):
    return queryset._meta.verbose_name_plural


@register.simple_tag
def get_verbose_name(queryset):
    return queryset._meta.verbose_name
