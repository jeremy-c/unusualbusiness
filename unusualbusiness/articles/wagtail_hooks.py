from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from django.utils.translation import ugettext as _

from django.utils.safestring import mark_safe
from django.utils.html import format_html, format_html_join
from django.conf import settings
from wagtail.wagtailcore import hooks
from wagtail.wagtailcore.whitelist import attribute_rule, check_url, allow_without_attributes

from .models import TheoryArticlePage, StoryArticlePage, NewsArticlePage, AuthorPage


class TheoryArticlePageModelAdmin(ModelAdmin):
    model = TheoryArticlePage
    menu_label = 'Theories' # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', )
    list_filter = ('live', )
    search_fields = ('title',)


class StoryArticlePageModelAdmin(ModelAdmin):
    model = StoryArticlePage
    menu_label = 'Stories' # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', )
    list_filter = ('live', )
    search_fields = ('title',)


class NewsArticlePageModelAdmin(ModelAdmin):
    model = NewsArticlePage
    menu_label = _('News and reports') # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', )
    list_filter = ('live', )
    search_fields = ('title',)


class AuthorPageModelAdmin(ModelAdmin):
    model = AuthorPage
    menu_label = 'Authors' # ditch this to use verbose_name_plural from model
    menu_icon = 'user' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', )
    search_fields = ('title',)


class ArticlePageTypesAdminGroup(ModelAdminGroup):
    menu_label = 'Articles'
    menu_icon = 'doc-full-inverse' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
        TheoryArticlePageModelAdmin,
        StoryArticlePageModelAdmin,
        NewsArticlePageModelAdmin,
        AuthorPageModelAdmin
    )

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(ArticlePageTypesAdminGroup)


# Hooks


@hooks.register('construct_whitelister_element_rules')
def whitelister_element_rules():
    return {
        'blockquote': attribute_rule({'class': True}),
    }


@hooks.register('insert_editor_js')
def editor_js():
    js_files = [
        'scripts/backend/hallo-custombuttons.js',
    ]
    js_includes = format_html_join(
        '\n',
        '<script src="{0}{1}"></script>',
        ((settings.STATIC_URL, filename) for filename in js_files)
    )

    return js_includes + format_html(
        """
        <script>
            registerHalloPlugin('blockquotebutton');
            //registerHalloPlugin('blockquotebuttonwithclass');
        </script>
        """
    )


@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        '<link rel="stylesheet" href="' + settings.STATIC_URL + 'bower_components/font-awesome/css/font-awesome.min.css">')

