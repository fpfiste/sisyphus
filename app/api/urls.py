from django.urls import include, path
from rest_framework import routers

from api.viewsets import *

router = routers.DefaultRouter()
router.register(r'company',  CompanyViewSet)
router.register(r'currency',  CurrencyViewSet)
router.register(r'asset/absence/code',  AssetAbsenceCodesViewSet)
router.register(r'asset/absence',  AssetAbsenceViewSet)
router.register(r'asset/type',  AssetTypesViewSet)
router.register(r'asset',  AssetViewSet)
router.register(r'employee/absence/code',  EmployeeAbsenceCodesViewSet)
router.register(r'employee/absence',  EmployeeAbsenceViewSet)
router.register(r'employee/types',  EmployeeTypesViewSet)
router.register(r'employee',  EmployeeViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]