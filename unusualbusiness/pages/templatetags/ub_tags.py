from datetime import date
from django import template
from django.conf import settings
from wagtail.wagtailcore.models import Page

register = template.Library()


# settings value
@register.assignment_tag
def get_google_maps_key():
    return getattr(settings, 'GOOGLE_MAPS_KEY', "")


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


@register.simple_tag(takes_context=True)
def localeurl(context, page):
    """
    Outputs a page's URL as relative (/foo/bar/) if it's within the same site as the
    current page, or absolute (http://example.com/foo/bar/) if not.
    """
    return  page.relative_url(context['request'].site)


@register.simple_tag(takes_context=True)
def pageurl(context, page):
    """
    Outputs a page's URL as relative (/foo/bar/) if it's within the same site as the
    current page, or absolute (http://example.com/foo/bar/) if not.
    """
    return page.relative_url(context['request'].site)


@register.simple_tag(takes_context=True)
def slugurl(context, slug):
    """Returns the URL for the page that has the given slug."""
    page = Page.objects.filter(slug=slug).first()

    if page:
        return page.specific.url_path
    else:
        return None


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('blocks/footer.html', takes_context=True)
def footer_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)
    about_page = menuitems.filter(slug='about').first()
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        'about_page': about_page,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('blocks/navbar.html', takes_context=True)
def navbar_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)

    about_page = menuitems.filter(slug='about').first()
    research_overview = menuitems.filter(slug='research-overview').first()

    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        'about_page': about_page,
        'research_overview': research_overview,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }



@register.simple_tag(takes_context=True)
def slugname(context, slug):
    """Returns the URL for the page that has the given slug."""
    page = Page.objects.filter(slug=slug).first()

    if page:
        return page.specific.title
    else:
        return None


@register.simple_tag(takes_context=True)
def parenturl(context, slug):
    """Returns the URL for the page that has the given slug."""
    page = Page.objects.filter(slug=slug).first()

    if page:
        return page.specific.url_path
    else:
        return None


@register.simple_tag(takes_context=True)
def parentname(context, slug):
        """Returns the URL for the page that has the given slug."""
        page = Page.objects.filter(slug=slug).first()

        if page:
            return page.specific.title
        else:
            return None

# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('blocks/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('blocks/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }
