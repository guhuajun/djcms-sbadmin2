# -*- coding: utf-8 -*-
# pylint: disable=E0401, C0111, R0903

from django.contrib.admin import AdminSite
from django.conf.urls import url
from django_cas_ng import views as cas_views


class SBAdminSite(AdminSite):
    '''Custom admin site to change login url'''

    def get_urls(self):

        urls = super(SBAdminSite, self).get_urls()
        return urls
