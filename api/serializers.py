# -*- coding: utf-8 -*-
# pylint: disable=E0401, C0111, R0903, C1001, W0232

'''
Dashboard Panel Data Model Serializer
'''


from rest_framework import serializers
from api import models


class DashboardPanelDataSourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DashboardPanelDataSource
