from wagtailmodeladmin.options import (
    ModelAdmin, ModelAdminGroup, wagtailmodeladmin_register)
from django.utils.translation import ugettext as _

from .models import TheoryArticlePage, StoryArticlePage, NewsArticlePage, AuthorPage


class TheoryArticlePageModelAdmin(ModelAdmin):
    model = TheoryArticlePage
    menu_label = 'Theories' # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse theories' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', )
    list_filter = ('live', )
    search_fields = ('title',)


class StoryArticlePageModelAdmin(ModelAdmin):
    model = StoryArticlePage
    menu_label = 'Stories' # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse story' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', )
    list_filter = ('live', )
    search_fields = ('title',)


class NewsArticlePageModelAdmin(ModelAdmin):
    model = NewsArticlePage
    menu_label = _('News and reports') # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse news' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', )
    list_filter = ('live', )
    search_fields = ('title',)


class AuthorPageModelAdmin(ModelAdmin):
    model = AuthorPage
    menu_label = 'Authors' # ditch this to use verbose_name_plural from model
    menu_icon = 'user author' # change as required
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
wagtailmodeladmin_register(ArticlePageTypesAdminGroup)
