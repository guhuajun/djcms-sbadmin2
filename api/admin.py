# -*- coding: utf-8 -*-
# pylint: disable=E0401, C0111, R0903

'''
Dashboard Panel Admin
'''

from django.contrib import admin
from api import models

admin.site.register(models.DashboardPanelDataSource)
