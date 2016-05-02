# -*- coding: utf-8 -*-
# pylint: disable=E0401, C0111, R0903

'''
Side Bar Menu Plugin
'''

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import SidebarMenuItem, SidebarParentMenu


class SidebarParentMenuPlugin(CMSPluginBase):
    '''
    Sidebar Parent Menu Plugin
    '''

    render_template = 'sidebar_parent.html'
    name = _('Sidebar Menu Parent')
    model = SidebarParentMenu
    allow_children = True
    child_classes = ['SidebarMenuItemPlugin']

    def render(self, context, instance, placeholder):
        context = super(SidebarParentMenuPlugin, self).render(
            context, instance, placeholder)
        return context


class SidebarMenuItemPlugin(CMSPluginBase):
    '''
    Sidebar Menu Item Plugin
    '''

    render_template = 'sidebar_child.html'
    name = _('Sidebar Menu Item')
    model = SidebarMenuItem
    require_parent = True
    parent_classes = ['SidebarParentMenuPlugin']

    def render(self, context, instance, placeholder):
        context = super(SidebarMenuItemPlugin, self).render(
            context, instance, placeholder)
        return context

plugin_pool.register_plugin(SidebarParentMenuPlugin)
plugin_pool.register_plugin(SidebarMenuItemPlugin)
