from django.db import models
from . import EmployeeAbsenceCodes


class EmployeeAbsences(models.Model):
    id_employee_absence = models.AutoField(primary_key=True)
    from_field = models.DateTimeField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.DateTimeField()
    fk_employee = models.ForeignKey('Employees', models.DO_NOTHING, db_column='fk_employee')
    fk_employee_absence_code = models.ForeignKey(EmployeeAbsenceCodes, models.DO_NOTHING, db_column='fk_employee_absence_code')

    class Meta:
        managed = False
        db_table = 'employee_absences'
