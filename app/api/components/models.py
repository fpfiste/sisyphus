# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AssetAbsenceCodes(models.Model):
    id_asset_absence_code = models.AutoField(primary_key=True)
    asset_absence_code = models.CharField()
    asset_absence_code_abbreviation = models.CharField()

    class Meta:
        managed = False
        db_table = 'asset_absence_codes'


class AssetAbsences(models.Model):
    id_asset_absence = models.AutoField(primary_key=True)
    from_field = models.DateTimeField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.DateTimeField()
    fk_asset = models.ForeignKey('Assets', models.DO_NOTHING, db_column='fk_asset')
    fk_asset_absence_code = models.ForeignKey(AssetAbsenceCodes, models.DO_NOTHING, db_column='fk_asset_absence_code')

    class Meta:
        managed = False
        db_table = 'asset_absences'


class AssetTaskAllocation(models.Model):
    id_asset_task_allocation = models.AutoField()
    fk_asset = models.IntegerField(primary_key=True)  # The composite primary key (fk_asset, fk_task) found, that is not supported. The first column is selected.
    fk_task = models.ForeignKey('Tasks', models.DO_NOTHING, db_column='fk_task')

    class Meta:
        managed = False
        db_table = 'asset_task_allocation'
        unique_together = (('fk_asset', 'fk_task'),)


class AssetTypes(models.Model):
    id_asset_type = models.AutoField(primary_key=True)
    asset_type = models.CharField()
    max_capacity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset_types'


class Assets(models.Model):
    id_asset = models.AutoField(primary_key=True)
    fk_asset_type = models.ForeignKey(AssetTypes, models.DO_NOTHING, db_column='fk_asset_type')
    asset_description = models.CharField()
    asset_internal_alias = models.CharField()
    year_of_production = models.IntegerField(blank=True, null=True)
    fk_sys_rec_state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'assets'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    fk_employee = models.IntegerField(blank=True, null=True)
    fk_language = models.ForeignKey('SysLanguage', models.DO_NOTHING, db_column='fk_language', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Companies(models.Model):
    id_company = models.AutoField(primary_key=True)
    company_name = models.CharField()
    company_street = models.CharField()
    company_zipcode = models.CharField()
    company_country = models.CharField()
    company_city = models.CharField()
    company_internal_alias = models.CharField(unique=True)
    fk_sys_rec_status = models.IntegerField()
    company_email = models.CharField(blank=True, null=True)
    is_customer = models.BooleanField(blank=True, null=True)
    is_supplier = models.BooleanField(blank=True, null=True)
    is_subcontractor = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class Currencies(models.Model):
    id_currency = models.AutoField(primary_key=True)
    currency = models.CharField()
    currency_abbreviation = models.CharField()
    currency_account_nr = models.CharField()

    class Meta:
        managed = False
        db_table = 'currencies'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmployeeAbsenceCodes(models.Model):
    id_employee_absence_code = models.AutoField(primary_key=True)
    employee_absence_code = models.CharField()
    employee_absence_code_abbreviation = models.CharField()

    class Meta:
        managed = False
        db_table = 'employee_absence_codes'


class EmployeeAbsences(models.Model):
    id_employee_absence = models.AutoField(primary_key=True)
    from_field = models.DateTimeField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.DateTimeField()
    fk_employee = models.ForeignKey('Employees', models.DO_NOTHING, db_column='fk_employee')
    fk_employee_absence_code = models.ForeignKey(EmployeeAbsenceCodes, models.DO_NOTHING, db_column='fk_employee_absence_code')

    class Meta:
        managed = False
        db_table = 'employee_absences'


class EmployeeTaskAllocation(models.Model):
    id_employee_task_allocation = models.AutoField()
    fk_employee = models.IntegerField(primary_key=True)  # The composite primary key (fk_employee, fk_task) found, that is not supported. The first column is selected.
    fk_task = models.ForeignKey('Tasks', models.DO_NOTHING, db_column='fk_task')

    class Meta:
        managed = False
        db_table = 'employee_task_allocation'
        unique_together = (('fk_employee', 'fk_task'),)


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
        db_table = 'employees'


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


class SysLanguage(models.Model):
    id_language = models.AutoField(primary_key=True)
    language_abbreviation = models.CharField(max_length=3)
    language = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sys_language'


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
    internal_info = models.CharField(blank=True, null=True)
    customer_reference = models.CharField(blank=True, null=True)
    fk_subcontractor = models.IntegerField(blank=True, null=True)
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
