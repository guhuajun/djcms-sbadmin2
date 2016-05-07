# encoding: utf-8
# pylint: disable=E0401, C0111, R0903, C1001, W0232, R0901, E1101

'''
Dashboard Panel Data Model Serializer
'''


from rest_framework import viewsets
from api import models, serializers


class DashboardPanelDataSourceViewSet(viewsets.ModelViewSet):

    queryset = models.DashboardPanelDataSource.objects.all()
    serializer_class = serializers.DashboardPanelDataSourceSerializer
