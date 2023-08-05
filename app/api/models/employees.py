from django.db import models
from . import EmployeeTypes


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
        db_table = 'employees'