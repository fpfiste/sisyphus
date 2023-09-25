from django.contrib import admin
from django.contrib.auth.management import create_permissions
from django.apps import apps

from .models import *






admin.site.register(EmployeeTypes)
admin.site.register(SysRecStates)
admin.site.register(TaskStates)
admin.site.register(SalesState)
admin.site.register(InvoiceStates)
admin.site.register(AssetTypes)
admin.site.register(EmployeeAbsenceCodes)
admin.site.register(AssetAbsenceCodes)
admin.site.register(Currencies)
admin.site.register(InvoiceTerms)
admin.site.register(Vat)
admin.site.register(Units)



