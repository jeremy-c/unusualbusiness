from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from unusualbusiness.howtos.models import HowToPage


class HowToPageModelAdmin(ModelAdmin):
    model = HowToPage
    menu_label = 'Knowledge pools' # ditch this to use verbose_name_plural from model
    menu_icon = 'radio-empty howtos' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', )
    list_filter = ('live', )
    search_fields = ('title',)

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(HowToPageModelAdmin)
