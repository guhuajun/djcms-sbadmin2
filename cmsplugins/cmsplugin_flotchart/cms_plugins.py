# -*- coding: utf-8 -*-
# pylint: disable=E0401, C0111, R0903

'''
Dashboard Panel Plugin
'''

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import FlotChartModel


class FlotChartPlugin(CMSPluginBase):
    '''
    Flot chart Plugin
    '''

    render_template = 'flot_chart.html'
    name = _('Flot Chart Plugin')
    model = FlotChartModel
    cache = False

    def render(self, context, instance, placeholder):
        context = super(FlotChartPlugin, self).render(
            context, instance, placeholder)
        return context

plugin_pool.register_plugin(FlotChartPlugin)
