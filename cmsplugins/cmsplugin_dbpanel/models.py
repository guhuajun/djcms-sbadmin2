# -*- coding: utf-8 -*-
# pylint: disable=E0401, C0111, R0903

'''
Dashboard Panel Model
'''


from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DashboardPanelModel(CMSPlugin):

    PANEL_CLASSES = (
        ('default', _('default')),
        ('primary', _('primary')),
        ('success', _('success')),
        ('info', _('info')),
        ('warning', _('warning')),
        ('danger', _('danger')),
        ('green', _('green')),
        ('yellow', _('yellow')),
        ('red', _('red')),
    )

    description = models.CharField(
        max_length=20, verbose_name=_("description"))
    panel_class = models.CharField(
        max_length=10, default="default", choices=PANEL_CLASSES, verbose_name=_("panel class"))
    icon_class = models.CharField(
        max_length=40, default="fa fa-bar-chart-o fa-fw", verbose_name=_("icon class"))
    data_source = models.URLField(verbose_name=_("data source"))

    def __unicode__(self):
        return u"{0}".format(self.description)
