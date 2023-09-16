from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'companies',  CompanyViewSet, basename='companies')
router.register(r'currencies',  CurrencyViewSet)
router.register(r'assets/absences/codes',  AssetAbsenceCodesViewSet)
router.register(r'assets/absences',  AssetAbsenceViewSet)
router.register(r'assets/types',  AssetTypesViewSet)
router.register(r'assets',  AssetViewSet)
router.register(r'employees/absences/codes',  EmployeeAbsenceCodesViewSet)
router.register(r'employees/absences',  EmployeeAbsenceViewSet)
router.register(r'employees/types',  EmployeeTypesViewSet)
router.register(r'employees',  EmployeeViewSet)
router.register(r'invoice-states',  InvoiceStateViewSet)
router.register(r'invoiceterms',  InvoiceTermsViewSet)
router.register(r'invoices',  InvoiceViewSet)
router.register(r'projects',  ProjectViewSet)
router.register(r'sales',  SalesViewSet)
router.register(r'sales-state',  SalesStateViewSet)
router.register(r'sysrecstate',  SysRecStateViewSet, basename='sysrecstate')
router.register(r'task-state',  TaskStateViewSet)
router.register(r'templates',  TaskTemplateViewSet)
router.register(r'tasks',  TaskViewSet)
router.register(r'units',  UnitViewSet)
router.register(r'vat',  VATViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

try:
    urlpatterns = [
        path('', include(router.urls)),

    ]
except:
    urlpatterns = []