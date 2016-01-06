from wagtailmodeladmin.options import (
    ModelAdmin, ModelAdminGroup, wagtailmodeladmin_register)
from django.utils.translation import ugettext as _

from .models import DefinitionPage, TheoryArticlePage, StoryArticlePage, ReportArticlePage


class TheoryArticlePageModelAdmin(ModelAdmin):
    model = TheoryArticlePage
    menu_label = 'Theories' # ditch this to use verbose_name_plural from model
    menu_icon = 'theories' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', )
    list_filter = ('live', )
    search_fields = ('title',)


class StoryArticlePageModelAdmin(ModelAdmin):
    model = StoryArticlePage
    menu_label = 'Stories' # ditch this to use verbose_name_plural from model
    menu_icon = 'story' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', )
    list_filter = ('live', )
    search_fields = ('title',)


class ReportArticlePageModelAdmin(ModelAdmin):
    model = ReportArticlePage
    menu_label = _('Event reports') # ditch this to use verbose_name_plural from model
    menu_icon = 'event-report' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', )
    list_filter = ('live', )
    search_fields = ('title',)


class DefinitionPageModelAdmin(ModelAdmin):
    model = DefinitionPage
    menu_label = 'Definitions' # ditch this to use verbose_name_plural from model
    menu_icon = 'definition' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', )
    list_filter = ('live', )
    search_fields = ('title',)


class ArticlePageTypesAdminGroup(ModelAdminGroup):
    menu_label = 'Articles'
    menu_icon = 'folder-open-inverse' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
        TheoryArticlePageModelAdmin,
        StoryArticlePageModelAdmin,
        ReportArticlePageModelAdmin,
        DefinitionPageModelAdmin
    )

# Now you just need to register your customised ModelAdmin class with Wagtail
wagtailmodeladmin_register(ArticlePageTypesAdminGroup)


