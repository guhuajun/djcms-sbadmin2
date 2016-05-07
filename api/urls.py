# encoding: utf-8
# pylint: disable=C0103

from rest_framework import routers
from api import views

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'panels', views.DashboardPanelDataSourceViewSet)

urlpatterns = router.urls
