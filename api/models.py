# -*- coding: utf-8 -*-
# pylint: disable=E0401, C0111, R0903

'''
Dashboard Panel Data Model
'''

from django.db import models


class DashboardPanelDataSource(models.Model):

    number = models.CharField(max_length=10)
    category_name = models.CharField(max_length=40)
    detail_link = models.URLField()

    def __unicode__(self):
        return u"{0} {1}".format(self.number, self.category_name)
