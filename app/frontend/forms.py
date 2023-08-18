from django.forms import ModelForm
from api.models import *

class CompanyForm(ModelForm):
    class Meta:
        model = Companies
        fields = '__all__'

class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'

class TaskForm(ModelForm):
    class Meta:
        model = Companies
        fields = '__all__'

class SalesForm(ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'

class EmployeeForm(ModelForm):
    class Meta:
        model = Companies
        fields = '__all__'

class AssetForm(ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'

class InvoiceForm(ModelForm):
    class Meta:
        model = Companies
        fields = '__all__'

