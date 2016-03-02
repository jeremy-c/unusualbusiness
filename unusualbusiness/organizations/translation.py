from .models import OrganizationPage, OrganizationIndexPage
from wagtail_modeltranslation.translator import TranslationOptions
from wagtail_modeltranslation.decorators import register


@register(OrganizationPage)
class OrganizationPageTR(TranslationOptions):
    fields = (
        'title',
        'slug',
        'description',
    )


@register(OrganizationIndexPage)
class OrganizationIndexPageTR(TranslationOptions):
    fields = (
    )