from django.db import models


class Tasks(models.Model):
    id_task = models.AutoField(primary_key=True)
    fk_project = models.ForeignKey('Projects', models.DO_NOTHING, db_column='fk_project')
    fk_task_state = models.ForeignKey('TaskStates', models.DO_NOTHING, db_column='fk_task_state')
    timestamp_from = models.DateTimeField(blank=True, null=True)
    timestamp_to = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    task_description = models.CharField()
    fk_invoice = models.IntegerField(blank=True, null=True)
    fk_unit = models.IntegerField(blank=True, null=True)
    fk_asset_allocation = models.IntegerField(blank=True, null=True)
    internal_info = models.CharField(blank=True, null=True)
    customer_reference = models.CharField(blank=True, null=True)
    fk_subcontractor = models.IntegerField(blank=True, null=True)
    brokerage_fee = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fk_service_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tasks'