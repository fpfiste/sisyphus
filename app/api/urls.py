from django.urls import include, path
from rest_framework import routers

from api.viewsets import *

router = routers.DefaultRouter()
router.register(r'companies',  CompanyViewSet)
router.register(r'currency',  CurrencyViewSet)
router.register(r'asset/absence/code',  AssetAbsenceCodesViewSet)
router.register(r'asset/absence',  AssetAbsenceViewSet)
router.register(r'asset/type',  AssetTypesViewSet)
router.register(r'assets',  AssetViewSet)
router.register(r'employee/absence/code',  EmployeeAbsenceCodesViewSet)
router.register(r'employee/absence',  EmployeeAbsenceViewSet)
router.register(r'employee/types',  EmployeeTypesViewSet)
router.register(r'employees',  EmployeeViewSet)
router.register(r'invoice/states',  InvoiceStateViewSet)
router.register(r'invoice/texts',  InvoiceStateViewSet)
router.register(r'invoice',  InvoiceViewSet)
router.register(r'invoice/paymentcondition',  PaymentConditionViewSet)
router.register(r'projects',  ProjectViewSet)
router.register(r'project/sales',  SalesViewSet)
router.register(r'sysrecstate',  SysRecStateViewSet)
router.register(r'project/task/state',  SysRecStateViewSet)
router.register(r'project/task/template',  TaskTemplateViewSet)
router.register(r'project/tasks',  TaskViewSet)
router.register(r'units',  UnitViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),

]