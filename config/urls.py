# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls.static import static
from django.views import defaults as default_views

from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from wagtail.contrib.wagtailapi import urls as wagtailapi_urls

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtailsearch import urls as wagtailsearch_urls


urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^api/', include(wagtailapi_urls)),
]

urlpatterns += i18n_patterns(
    url(r'^search/', include(wagtailsearch_urls)),
    #url(r'', include('myapp.urls')), # Optional URL for including your own vanilla Django urls/views
    url(r'', include(wagtail_urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
