from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # Helper Class for creating user admin pages
from django.contrib.auth.forms import UserCreationForm

from .models import *

admin.site.register(Employees)
admin.site.register(Units)
admin.site.register(Currencies)
admin.site.register(Vat)
admin.site.register(TaskStates)
admin.site.register(SalesState)


