# encoding: utf-8
# pylint: disable=E0401, C0111, R0903, C1001, W0232, R0901, E1101

'''
Dashboard Panel Data Model Serializer
'''

import math
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from api import models, serializers


class DashboardPanelDataSourceViewSet(viewsets.ModelViewSet):

    queryset = models.DashboardPanelDataSource.objects.all()
    serializer_class = serializers.DashboardPanelDataSourceSerializer


class FlotChart1(APIView):

    def get(self, request, format=None):
        response_data = {
            "data": [(x*0.1, float(math.sin(x*0.1))) for x in xrange(-30, 31)]
        }
        return Response(response_data)
