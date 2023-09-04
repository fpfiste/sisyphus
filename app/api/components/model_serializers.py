from rest_framework import serializers
from .models import *


class AssetAbsenceCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetAbsenceCodes
        fields = '__all__'

class AssetAbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetAbsences
        fields = '__all__'


class AssetTaskAllocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssetTaskAllocation
        fields = '__all__'

class AssetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetTypes
        fields = '__all__'


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = '__all__'

class SysRecStatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysRecStates
        fields = ('id_sys_rec_status', 'sys_rec_status')

class CompanySerializer(serializers.ModelSerializer):
    fk_sys_rec_status = SysRecStatesSerializer()

    class Meta:
        model = Companies
        fields = ['id_company', 'company_name', 'company_street', 'company_zipcode','company_country','company_city','company_internal_alias', 'fk_sys_rec_status', 'company_email', 'is_customer', 'is_supplier', 'is_subcontractor']

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = '__all__'

class EmployeeAbsenceCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAbsenceCodes
        fields = '__all__'

class EmployeeAbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAbsences
        fields = '__all__'

class EmployeeTaskAllocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeTaskAllocation
        fields = '__all__'


class EmployeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTypes
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'



class InvoiceStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceStates
        fields = '__all__'

class InvoiceTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceTexts
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoices
        fields = '__all__'

class PaymentConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentConditions
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

class SysRecStatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysRecStates
        fields = '__all__'

class TaskStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStates
        fields = '__all__'

class TaskTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTemplates
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Units
        fields = '__all__'