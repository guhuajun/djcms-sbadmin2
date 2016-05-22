# -*- coding: utf-8 -*-
# pylint: disable=E0401, W0401, W0614, C0103

from __future__ import absolute_import, print_function, unicode_literals

import debug_toolbar
from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.authtoken import views

admin.autodiscover()

urlpatterns = i18n_patterns('',
                            url(r'^admin/', include(admin.site.urls)),
                            url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
                                {'sitemaps': {'cmspages': CMSSitemap}}),
                            url(r'^select2/', include('django_select2.urls')),
                            url(r'^', include('cms.urls')),
                           )

urlpatterns += patterns('',
                        url(r'^api/', include('api.urls')),

                        # Rest API authentication
                        url(r'^api/api-auth/', include('rest_framework.urls',
                                                       namespace='rest_framework')),

                        # Token Infra
                        url(r'^api/token/', views.obtain_auth_token),

                       )

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
                           url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                               {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                          ) + staticfiles_urlpatterns() + urlpatterns

    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                           )
