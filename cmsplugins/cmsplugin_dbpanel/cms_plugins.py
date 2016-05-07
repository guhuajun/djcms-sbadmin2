# -*- coding: utf-8 -*-
# pylint: disable=E0401, C0111, R0903

'''
Dashboard Panel Plugin
'''

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import DashboardPanelModel


class DashboardPanelPlugin(CMSPluginBase):
    '''
    Dashboard Panel Plugin
    '''

    render_template = 'dashboard_panel.html'
    name = _('Dashboard Panel Plugin')
    model = DashboardPanelModel

    def render(self, context, instance, placeholder):
        context = super(DashboardPanelPlugin, self).render(
            context, instance, placeholder)
        return context

plugin_pool.register_plugin(DashboardPanelPlugin)
