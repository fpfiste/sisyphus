from django.db import models





class EmployeeTypes(models.Model):
    id_employee_type = models.AutoField(primary_key=True)
    employee_type_description = models.CharField()

    class Meta:
        managed = False
        db_table = 'employee_types'