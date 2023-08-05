# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class InvoiceStates(models.Model):
    id_invoice_state = models.AutoField(primary_key=True)
    invoice_state = models.CharField()
    invoice_state_abbreviation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_states'


class InvoiceTexts(models.Model):
    id_invoice_text = models.AutoField(primary_key=True)
    invoice_text = models.CharField()
    fk_customer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_texts'


class Invoices(models.Model):
    id_invoice = models.AutoField(primary_key=True)
    invoice_date = models.DateField(blank=True, null=True)
    fk_invoice_text = models.ForeignKey(InvoiceTexts, models.DO_NOTHING, db_column='fk_invoice_text', blank=True, null=True)
    fk_invoice_state = models.ForeignKey(InvoiceStates, models.DO_NOTHING, db_column='fk_invoice_state')
    fk_payment_conditions = models.ForeignKey('PaymentConditions', models.DO_NOTHING, db_column='fk_payment_conditions')

    class Meta:
        managed = False
        db_table = 'invoices'


class PaymentConditions(models.Model):
    id_payment_condition = models.AutoField(primary_key=True)
    vat = models.DecimalField(max_digits=65535, decimal_places=65535)
    fk_currency = models.ForeignKey(Currencies, models.DO_NOTHING, db_column='fk_currency')
    due_days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payment_conditions'


class Projects(models.Model):
    id_project = models.AutoField(primary_key=True)
    project_name = models.CharField()
    fk_customer = models.IntegerField()
    planned_start_date = models.DateField()
    planned_end_date = models.DateField()
    effective_start_date = models.DateField(blank=True, null=True)
    effective_end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'


class Sales(models.Model):
    id_sale = models.AutoField(primary_key=True)
    sale_timestamp = models.DateTimeField()
    fk_project = models.ForeignKey(Projects, models.DO_NOTHING, db_column='fk_project')
    sale_amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    sale_unit_price = models.DecimalField(max_digits=65535, decimal_places=65535)
    sales_reference = models.CharField()
    fk_unit = models.IntegerField()
    fk_product = models.IntegerField()
    fk_invoice = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sales'


class SysRecStates(models.Model):
    id_sys_rec_status = models.AutoField(primary_key=True)
    sys_rec_status = models.CharField()

    class Meta:
        managed = False
        db_table = 'sys_rec_states'


class TaskStates(models.Model):
    id_task_state = models.AutoField(primary_key=True)
    task_state = models.CharField()

    class Meta:
        managed = False
        db_table = 'task_states'


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


class Tasks(models.Model):
    id_task = models.AutoField(primary_key=True)
    fk_project = models.ForeignKey(Projects, models.DO_NOTHING, db_column='fk_project')
    fk_task_state = models.ForeignKey(TaskStates, models.DO_NOTHING, db_column='fk_task_state')
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


class Units(models.Model):
    id_unit = models.AutoField(primary_key=True)
    unit = models.CharField()
    unit_abbreviation = models.CharField()

    class Meta:
        managed = False
        db_table = 'units'
