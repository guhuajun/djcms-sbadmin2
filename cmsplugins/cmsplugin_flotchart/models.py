# -*- coding: utf-8 -*-
# pylint: disable=E0401, C0111, R0903

'''
Flot Chart Model
'''


from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class FlotChartModel(CMSPlugin):

    description = models.CharField(
        max_length=20, verbose_name=_("description"))
    data_source = models.URLField(verbose_name=_("data source"))
    refresh_interval = models.PositiveSmallIntegerField(
        default=5000, verbose_name=_("refresh interval"))

    def __unicode__(self):
        return u"{0}".format(self.description)
