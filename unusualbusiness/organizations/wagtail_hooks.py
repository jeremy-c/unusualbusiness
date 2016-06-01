from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import OrganizationPage


class OrganizationPageModelAdmin(ModelAdmin):
    model = OrganizationPage
    menu_icon = 'group' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', )
    list_filter = ('live', )
    search_fields = ('title',)

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(OrganizationPageModelAdmin)
