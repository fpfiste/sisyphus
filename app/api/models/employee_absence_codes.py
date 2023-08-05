from django.db import models


class EmployeeAbsenceCodes(models.Model):
    id_employee_absence_code = models.AutoField(primary_key=True)
    employee_absence_code = models.CharField()
    employee_absence_code_abbreviation = models.CharField()

    class Meta:
        managed = False
        db_table = 'employee_absence_codes'