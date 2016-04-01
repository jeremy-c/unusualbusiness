from wagtailmodeladmin.options import (
    ModelAdmin, ModelAdminGroup, wagtailmodeladmin_register)
from django.utils.translation import ugettext as _

from .models import DefinitionPage


class DefinitionPageModelAdmin(ModelAdmin):
    model = DefinitionPage
    menu_label = 'Definitions' # ditch this to use verbose_name_plural from model
    menu_icon = 'help definition' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', )
    list_filter = ('live', )
    search_fields = ('title',)


# Now you just need to register your customised ModelAdmin class with Wagtail
wagtailmodeladmin_register(DefinitionPageModelAdmin)
