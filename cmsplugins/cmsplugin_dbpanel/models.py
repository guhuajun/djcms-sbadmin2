# -*- coding: utf-8 -*-
# pylint: disable=E0401, C0111, R0903

'''
Dashboard Panel Model
'''


from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DashboardPanelModel(CMSPlugin):
    description = models.CharField(
        max_length=20, verbose_name=_("description"))
    icon_class = models.CharField(
        max_length=40, default="fa fa-bar-chart-o fa-fw", verbose_name=_("icon class"))
    data_source = models.URLField(verbose_name=_("data source"))

    def __unicode__(self):
        return u"{0}".format(self.description)
