from django.db import models
from rest_framework import serializers, viewsets, permissions


class EmployeeTypes(models.Model):
    id_employee_type = models.AutoField(primary_key=True)
    employee_type_description = models.CharField()

    class Meta:
        managed = False
        db_table = 'employee_types'



class Employees(models.Model):
    id_employee = models.AutoField(primary_key=True)
    employee_first_name = models.CharField()
    employee_last_name = models.CharField()
    employee_street = models.CharField()
    employee_zipcode = models.CharField()
    employee_city = models.CharField()
    emplyee_email = models.CharField()
    employee_cell_phone = models.CharField()
    emplyee_birthday = models.DateField()
    emplyee_salary = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fk_employee_type = models.ForeignKey(EmployeeTypes, models.DO_NOTHING, db_column='fk_employee_type')
    employee_fte = models.DecimalField(max_digits=65535, decimal_places=65535)
    employee_internal_alias = models.CharField(unique=True)
    fk_sys_rec_status = models.IntegerField()
    employee_house_nr = models.CharField()

    class Meta:
        managed = False
        db_table = 'companies'

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fiels = [__all__]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Company.objects.all().order_by('id_company')
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]