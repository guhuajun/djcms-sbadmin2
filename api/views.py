# encoding: utf-8
# pylint: disable=E0401, C0111, R0903, C1001, W0232, R0901, E1101, W0613, R0201

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

    def get(self, request):
        data = []
        for x in xrange(0, 100):
            data.append([x*0.1, math.sin(x*0.1)])
        response_data = {
            "data": data,
            "label": "sin(x)"
        }
        return Response(response_data)
