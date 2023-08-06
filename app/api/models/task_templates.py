# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class TaskTemplates(models.Model):
    id_task_template = models.AutoField(primary_key=True)
    fk_customer = models.IntegerField()
    fk_unit = models.IntegerField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    unit_price = models.DecimalField(max_digits=65535, decimal_places=65535)
    task_description = models.CharField()

    class Meta:
        managed = False
        db_table = 'task_templates'