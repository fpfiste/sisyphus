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
    asset_absence_code = models.CharField(max_length=30)
    asset_absence_code_abbreviation = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'asset_absence_codes'


class AssetAbsences(models.Model):
    id_asset_absence = models.AutoField(primary_key=True)
    asset_absence_date_from = models.DateField()
    asset_absence_date_to = models.DateField()
    fk_asset = models.ForeignKey('Assets', models.DO_NOTHING, db_column='fk_asset')
    fk_asset_absence_code = models.ForeignKey(AssetAbsenceCodes, models.DO_NOTHING, db_column='fk_asset_absence_code')
    asset_absence_time_from = models.TimeField()
    asset_absence_time_to = models.TimeField()

    class Meta:
        managed = False
        db_table = 'asset_absences'


class AssetTypes(models.Model):
    id_asset_type = models.AutoField(primary_key=True)
    asset_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'asset_types'


class Assets(models.Model):
    id_asset = models.AutoField(primary_key=True)
    asset_description = models.CharField(max_length=50)
    asset_internal_alias = models.CharField(max_length=20)
    fk_asset_type = models.ForeignKey(AssetTypes, models.DO_NOTHING, db_column='fk_asset_type')
    fk_sys_rec_status = models.ForeignKey('SysRecStates', models.DO_NOTHING, db_column='fk_sys_rec_status')
    custom_fields = models.JSONField(blank=True, null=True)
    fk_company = models.ForeignKey('Companies', models.DO_NOTHING, db_column='fk_company')

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
    avatar = models.CharField(blank=True, null=True)
    fk_employee = models.IntegerField(blank=True, null=True)

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
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Cancellations(models.Model):
    id_invoice_cancellation = models.AutoField(primary_key=True)
    cancellation_date = models.DateField()
    cancellation_time = models.TimeField()
    cancellation_reason = models.CharField(max_length=200)
    cancellation_user = models.CharField(max_length=20)
    fk_invoice = models.OneToOneField('Receivables', models.DO_NOTHING, db_column='fk_invoice')

    class Meta:
        managed = False
        db_table = 'cancellations'


class ClearingType(models.Model):
    id_clearing_type = models.AutoField(primary_key=True)
    clearing_type = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'clearing_type'


class Companies(models.Model):
    id_company = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    company_street = models.CharField(max_length=50)
    company_zipcode = models.CharField(max_length=50)
    fk_country = models.ForeignKey('Countries', models.DO_NOTHING, db_column='fk_country')
    company_city = models.CharField(max_length=50)
    company_internal_alias = models.CharField(unique=True, max_length=50)
    company_email = models.CharField(max_length=50, blank=True, null=True)
    is_customer = models.BooleanField(blank=True, null=True)
    is_supplier = models.BooleanField(blank=True, null=True)
    is_subcontractor = models.BooleanField(blank=True, null=True)
    fk_sys_rec_status = models.ForeignKey('SysRecStates', models.DO_NOTHING, db_column='fk_sys_rec_status')
    custom_fields = models.JSONField(blank=True, null=True)
    is_own_company = models.BooleanField(blank=True, null=True)
    vat_number = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    invoice_receiver = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class Config(models.Model):
    id_config = models.AutoField(primary_key=True)
    config_key = models.CharField()
    value_string = models.CharField(blank=True, null=True)
    value_bytes = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config'


class Countries(models.Model):
    id_country = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    country_code = models.CharField(max_length=3)
    emoji_code = models.CharField(max_length=10, blank=True, null=True)
    country_title = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Currencies(models.Model):
    id_currency = models.AutoField(primary_key=True)
    currency = models.CharField(max_length=50)
    currency_abbreviation = models.CharField(max_length=3)
    currency_account_nr = models.CharField(max_length=50)
    qr_iban = models.CharField(max_length=50)

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
    employee_absence_code = models.CharField(max_length=50)
    employee_absence_code_abbreviation = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'employee_absence_codes'


class EmployeeAbsences(models.Model):
    id_employee_absence = models.AutoField(primary_key=True)
    employee_absence_date_from = models.DateField()
    employee_absence_date_to = models.DateField()
    fk_employee = models.ForeignKey('Employees', models.DO_NOTHING, db_column='fk_employee')
    fk_employee_absence_code = models.ForeignKey(EmployeeAbsenceCodes, models.DO_NOTHING, db_column='fk_employee_absence_code')
    employee_absence_time_from = models.TimeField()
    employee_absence_time_to = models.TimeField()

    class Meta:
        managed = False
        db_table = 'employee_absences'


class EmployeeTypes(models.Model):
    id_employee_type = models.AutoField(primary_key=True)
    employee_type_description = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'employee_types'


class Employees(models.Model):
    id_employee = models.AutoField(primary_key=True)
    employee_first_name = models.CharField(max_length=50)
    employee_last_name = models.CharField(max_length=50)
    employee_street = models.CharField(max_length=50)
    employee_zipcode = models.CharField(max_length=20)
    employee_city = models.CharField(max_length=50)
    employee_email = models.CharField(max_length=50, blank=True, null=True)
    employee_cell_phone = models.CharField(max_length=50, blank=True, null=True)
    employee_birthday = models.DateField(blank=True, null=True)
    employee_salary = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    employee_fte = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    employee_internal_alias = models.CharField(unique=True, max_length=10)
    fk_employee_type = models.ForeignKey(EmployeeTypes, models.DO_NOTHING, db_column='fk_employee_type')
    fk_sys_rec_status = models.ForeignKey('SysRecStates', models.DO_NOTHING, db_column='fk_sys_rec_status')
    fk_country = models.ForeignKey(Countries, models.DO_NOTHING, db_column='fk_country')
    custom_fields = models.JSONField(blank=True, null=True)
    fk_company = models.ForeignKey(Companies, models.DO_NOTHING, db_column='fk_company')
    fk_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='fk_user', blank=True, null=True)
    avatar = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class InvoiceStates(models.Model):
    id_invoice_state = models.AutoField(primary_key=True)
    invoice_state = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'invoice_states'


class InvoiceTerms(models.Model):
    id_invoice_term = models.AutoField(primary_key=True)
    due_days = models.IntegerField(unique=True)
    term_title = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'invoice_terms'


class InvoiceTextTemplates(models.Model):
    id_invoice_text = models.AutoField(primary_key=True)
    invoice_text = models.CharField(max_length=200)
    fk_customer = models.ForeignKey(Companies, models.DO_NOTHING, db_column='fk_customer')
    invoice_text_title = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'invoice_text_templates'


class Payables(models.Model):
    id_payable = models.AutoField(primary_key=True)
    fk_company = models.ForeignKey(Companies, models.DO_NOTHING, db_column='fk_company')
    invoice_date = models.DateField()
    net_total = models.DecimalField(max_digits=11, decimal_places=2)
    vat = models.DecimalField(max_digits=11, decimal_places=2)
    fk_invoice_status = models.ForeignKey(InvoiceStates, models.DO_NOTHING, db_column='fk_invoice_status')
    fk_terms = models.ForeignKey(InvoiceTerms, models.DO_NOTHING, db_column='fk_terms')
    fk_currency = models.ForeignKey(Currencies, models.DO_NOTHING, db_column='fk_currency')
    positions = models.JSONField(blank=True, null=True)
    invoice_id = models.CharField(unique=True, max_length=200)
    total = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'payables'


class Projects(models.Model):
    id_project = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    fk_customer = models.ForeignKey(Companies, models.DO_NOTHING, db_column='fk_customer')
    fk_sys_rec_status = models.ForeignKey('SysRecStates', models.DO_NOTHING, db_column='fk_sys_rec_status')
    custom_fields = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'


class Receivables(models.Model):
    id_invoice = models.AutoField(primary_key=True)
    invoice_date = models.DateField()
    invoice_text = models.CharField(max_length=200, blank=True, null=True)
    fk_invoice_state = models.ForeignKey(InvoiceStates, models.DO_NOTHING, db_column='fk_invoice_state')
    fk_invoice_terms = models.ForeignKey(InvoiceTerms, models.DO_NOTHING, db_column='fk_invoice_terms')
    fk_vat = models.ForeignKey('Vat', models.DO_NOTHING, db_column='fk_vat')
    net_total = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    fk_currency = models.ForeignKey(Currencies, models.DO_NOTHING, db_column='fk_currency')
    fk_project = models.ForeignKey(Projects, models.DO_NOTHING, db_column='fk_project')
    discount = models.DecimalField(max_digits=3, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'receivables'


class RevenueType(models.Model):
    id_revenue_type = models.AutoField(primary_key=True)
    revenue_type = models.CharField(max_length=30)
    pl_account_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'revenue_type'


class Sales(models.Model):
    id_sale = models.AutoField(primary_key=True)
    sale_date = models.DateField()
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    unit_price = models.DecimalField(max_digits=11, decimal_places=2)
    customer_reference = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200)
    sale_time = models.TimeField()
    fk_currency = models.ForeignKey(Currencies, models.DO_NOTHING, db_column='fk_currency')
    fk_invoice = models.ForeignKey(Receivables, models.DO_NOTHING, db_column='fk_invoice', blank=True, null=True)
    fk_project = models.ForeignKey(Projects, models.DO_NOTHING, db_column='fk_project')
    fk_sales_status = models.ForeignKey('SalesState', models.DO_NOTHING, db_column='fk_sales_status')
    fk_unit = models.ForeignKey('Units', models.DO_NOTHING, db_column='fk_unit')
    fk_vat = models.ForeignKey('Vat', models.DO_NOTHING, db_column='fk_vat')
    custom_fields = models.JSONField(blank=True, null=True)
    fk_clearing_type = models.ForeignKey(ClearingType, models.DO_NOTHING, db_column='fk_clearing_type')
    fk_revenue_type = models.ForeignKey(RevenueType, models.DO_NOTHING, db_column='fk_revenue_type', blank=True, null=True)
    invoice_position_nr = models.IntegerField(blank=True, null=True)
    changed_on = models.DateTimeField(blank=True, null=True)
    changed_by = models.CharField(max_length=200, blank=True, null=True)
    #history = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales'


class SalesState(models.Model):
    id_sales_state = models.AutoField(primary_key=True)
    sales_state = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'sales_state'


class SysRecStates(models.Model):
    id_sys_rec_status = models.AutoField(primary_key=True)
    sys_rec_status = models.CharField(max_length=20)
    entity = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_rec_states'


class TaskStates(models.Model):
    id_task_state = models.AutoField(primary_key=True)
    task_state = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'task_states'


class Tasks(models.Model):
    id_task = models.AutoField(primary_key=True)
    task_date_from = models.DateField(blank=True, null=True)
    task_date_to = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=200)
    internal_info = models.CharField(max_length=200, blank=True, null=True)
    customer_reference = models.CharField(max_length=100, blank=True, null=True)
    task_time_from = models.TimeField(blank=True, null=True)
    task_time_to = models.TimeField(blank=True, null=True)
    fk_asset_1 = models.ForeignKey(Assets, models.DO_NOTHING, db_column='fk_asset_1', blank=True, null=True)
    fk_asset_2 = models.ForeignKey(Assets, models.DO_NOTHING, db_column='fk_asset_2', related_name='tasks_fk_asset_2_set', blank=True, null=True)
    fk_currency = models.ForeignKey(Currencies, models.DO_NOTHING, db_column='fk_currency', blank=True, null=True)
    fk_employee_1 = models.ForeignKey(Employees, models.DO_NOTHING, db_column='fk_employee_1', blank=True, null=True)
    fk_employee_2 = models.ForeignKey(Employees, models.DO_NOTHING, db_column='fk_employee_2', related_name='tasks_fk_employee_2_set', blank=True, null=True)
    fk_invoice = models.ForeignKey(Receivables, models.DO_NOTHING, db_column='fk_invoice', blank=True, null=True)
    fk_project = models.ForeignKey(Projects, models.DO_NOTHING, db_column='fk_project')
    fk_task_state = models.ForeignKey(TaskStates, models.DO_NOTHING, db_column='fk_task_state')
    fk_unit = models.ForeignKey('Units', models.DO_NOTHING, db_column='fk_unit', blank=True, null=True)
    fk_vat = models.ForeignKey('Vat', models.DO_NOTHING, db_column='fk_vat', blank=True, null=True)
    custom_fields = models.JSONField(blank=True, null=True)
    fk_clearing_type = models.ForeignKey(ClearingType, models.DO_NOTHING, db_column='fk_clearing_type', blank=True, null=True)
    fk_revenue_type = models.ForeignKey(RevenueType, models.DO_NOTHING, db_column='fk_revenue_type', blank=True, null=True)
    invoice_position_nr = models.IntegerField(blank=True, null=True)
    changed_on = models.DateTimeField(blank=True, null=True)
    changed_by = models.CharField(max_length=200, blank=True, null=True)
    #history = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasks'


class TemplateTypes(models.Model):
    id_template_type = models.AutoField(primary_key=True)
    template_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'template_types'


class Templates(models.Model):
    id_template = models.AutoField(primary_key=True)
    fk_project = models.ForeignKey(Projects, models.DO_NOTHING, db_column='fk_project', blank=True, null=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    fk_currency = models.ForeignKey(Currencies, models.DO_NOTHING, db_column='fk_currency', blank=True, null=True)
    fk_unit = models.ForeignKey('Units', models.DO_NOTHING, db_column='fk_unit', blank=True, null=True)
    fk_vat = models.ForeignKey('Vat', models.DO_NOTHING, db_column='fk_vat', blank=True, null=True)
    fk_template_type = models.ForeignKey(TemplateTypes, models.DO_NOTHING, db_column='fk_template_type', blank=True, null=True)
    template_title = models.CharField(max_length=50)
    fk_revenue_type = models.ForeignKey(RevenueType, models.DO_NOTHING, db_column='fk_revenue_type', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'templates'


class Units(models.Model):
    id_unit = models.AutoField(primary_key=True)
    unit = models.CharField(max_length=20)
    unit_abbreviation = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'units'


class Vat(models.Model):
    id_vat = models.AutoField(primary_key=True)
    vat = models.DecimalField(max_digits=3, decimal_places=3)
    vat_title = models.CharField(max_length=50)
    netto = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vat'
