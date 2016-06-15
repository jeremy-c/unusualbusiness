from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)
from .models import GeneralPage, StaticContent


class GeneralPageModelAdmin(ModelAdmin):
    model = GeneralPage
    menu_icon = 'doc-full' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', )
    list_filter = ('live', )
    search_fields = ('title',)


class StaticContentModelAdmin(ModelAdmin):
    model = StaticContent
    menu_icon = 'doc-full' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', )
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class SnippetsAdminGroup(ModelAdminGroup):
    menu_label = 'Snippets'
    menu_icon = 'snippet' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
        StaticContentModelAdmin,
        GeneralPageModelAdmin,
    )

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(SnippetsAdminGroup)

