from wagtailmodeladmin.options import ModelAdmin, wagtailmodeladmin_register
from .models import EventPage


class EventPageModelAdmin(ModelAdmin):
    model = EventPage
    menu_label = 'Events' # ditch this to use verbose_name_plural from model
    menu_icon = 'date' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', 'start_date', )
    list_filter = ('live', )
    search_fields = ('title',)

# Now you just need to register your customised ModelAdmin class with Wagtail
wagtailmodeladmin_register(EventPageModelAdmin)
