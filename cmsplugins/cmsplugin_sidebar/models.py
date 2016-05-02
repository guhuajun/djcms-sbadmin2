# -*- coding: utf-8 -*-
# pylint: disable=E0401, C0111, R0903

'''
Side Bar Menu Model
'''


from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class SidebarMenuItem(CMSPlugin):

    name = models.CharField(max_length=20)
    link = models.CharField(max_length=200, default='#')

    def __unicode__(self):
        return u"{0}".format(self.name)


class SidebarParentMenu(CMSPlugin):
    name = models.CharField(max_length=20)
    icon_class = models.CharField(max_length=40, default="fa fa-bar-chart-o fa-fw")
    link = models.CharField(max_length=200, default='#')
    sub_menus = models.ManyToManyField(SidebarMenuItem, blank=True)

    def copy_relations(self, oldinstance):
        self.sub_menus = oldinstance.sub_menus.all()

    def __unicode__(self):
        return u"{0}".format(self.name)
