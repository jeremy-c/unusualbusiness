from wagtailmodeladmin.options import ModelAdmin, wagtailmodeladmin_register

from howtos.models import HowToPage


class HowToPageModelAdmin(ModelAdmin):
    model = HowToPage
    menu_label = 'How to\'s' # ditch this to use verbose_name_plural from model
    menu_icon = 'howtos' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', )
    list_filter = ('live', )
    search_fields = ('title',)

# Now you just need to register your customised ModelAdmin class with Wagtail
wagtailmodeladmin_register(HowToPageModelAdmin)