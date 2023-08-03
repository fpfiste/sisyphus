# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models






class Currency(models.Model):
    id_currency = models.AutoField(primary_key=True)
    currency = models.CharField(max_length=10)
    currency_account_number = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'currency'

    def __str__(self):
        return self.currency


class Customer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    customer_company_name = models.CharField(max_length=100)
    customer_residence = models.CharField(max_length=100)
    fk_township = models.ForeignKey('Township', models.DO_NOTHING, db_column='fk_township')
    customer_email_contact = models.CharField(max_length=100)
    customer_internal_alias = models.CharField(unique=False, max_length=50)
    customer_invoice_text = models.CharField(max_length=2000)

    class Meta:
        managed = True
        db_table = 'customer'

    def __str__(self):
        return self.customer_internal_alias

class CustomerInvoiceText(models.Model):
    id_customer_invoice_text = models.AutoField(primary_key=True)
    customer_invoice_text = models.CharField(max_length=1000)
    fk_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='fk_customer')

    class Meta:
        managed = True
        db_table = 'customer_invoice_text'
    def __str__(self):
        return self.customer_invoice_text



class Employee(models.Model):
    id_employee = models.AutoField(primary_key=True)
    employee_last_name = models.CharField(max_length=100)
    employee_first_name = models.CharField(max_length=100)
    employee_residence = models.CharField(max_length=100)
    fk_township = models.ForeignKey('Township', models.DO_NOTHING, db_column='fk_township')
    employee_mobile = models.CharField(max_length=20)
    employee_email = models.CharField(max_length=200)
    employee_date_of_birth = models.DateField(blank=True, null=True)
    employee_internal_alias = models.CharField(unique=True, max_length=100, blank=True, null=True)
    fk_sys_dimension_status = models.ForeignKey('SysDimensionStatus', models.DO_NOTHING, db_column='fk_sys_dimension_status', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'employee'
    def __str__(self):
        return self.employee_internal_alias

class EmployeeAbsence(models.Model):
    fk_employee_absence_code = models.ForeignKey('EmployeeAbsenceCode', models.DO_NOTHING, db_column='fk_employee_absence_code')
    fk_employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='fk_employee')
    id_employee_absence = models.AutoField(primary_key=True)
    employee_absence_date_from = models.DateField()
    employee_absence_date_to = models.DateField()
    employee_absence_time_from = models.TimeField(blank=True, null=True)
    employee_absence_time_to = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'employee_absence'


class EmployeeAbsenceCode(models.Model):
    id_employee_absence_code = models.AutoField(primary_key=True)
    employee_absence_code = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'employee_absence_code'
    def __str__(self):
        return self.employee_absence_code

class Purchase(models.Model):
    id_purchase = models.AutoField(primary_key=True)
    purchase_date = models.DateField()
    purchase_time = models.TimeField()
    fk_service_status = models.ForeignKey('ServiceStatus', models.DO_NOTHING, db_column='fk_service_status')
    fk_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='fk_customer', blank=True, null=True)
    fk_invoice = models.ForeignKey('Invoice', models.DO_NOTHING, db_column='fk_invoice', blank=True, null=True)
    purchase_amount = models.FloatField()
    purchase_price = models.FloatField()
    purchase_description = models.CharField(max_length=100, blank=True, null=True)
    fk_fuel_station_key = models.ForeignKey('FuelStationKey', models.DO_NOTHING, db_column='fk_fuel_station_key', blank=True, null=True)
    fuel_purchase_file_path = models.CharField(max_length=1000, blank=True, null=True)
    fk_unit = models.ForeignKey('Unit', models.DO_NOTHING, db_column='fk_unit')
    fk_currency = models.ForeignKey(Currency, models.DO_NOTHING, db_column='fk_currency')
    fk_service_type = models.ForeignKey('ServiceType', models.DO_NOTHING, db_column='fk_service_type')
    fk_service_clearing_type = models.ForeignKey('ServiceClearingType', models.DO_NOTHING, db_column='fk_service_clearing_type', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fuel_purchase'
        unique_together = (('fk_service_type', 'fk_fuel_station_key', 'fuel_purchase_date', 'fuel_purchase_time', 'fuel_purchase_amount', 'fuel_purchase_price'),)


class FuelStationKey(models.Model):
    id_fuel_station_key = models.IntegerField(primary_key=True)
    fk_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='fk_customer', blank=True, null=True)
    fuel_station_key_holder_external = models.CharField(max_length=100, blank=True, null=True)
    fk_employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='fk_employee', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fuel_station_key'
    def __str__(self):
        return str(self.id_fuel_station_key)

class Invoice(models.Model):
    id_invoice = models.AutoField(primary_key=True)
    invoice_date = models.DateField()
    fk_invoice_status = models.ForeignKey('InvoiceStatus', models.DO_NOTHING, db_column='fk_invoice_status')
    invoice_total = models.FloatField(blank=True, null=True)
    invoice_payment_due_days = models.IntegerField()
    fk_currency = models.ForeignKey(Currency, models.DO_NOTHING, db_column='fk_currency')
    fk_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='fk_customer', blank=True, null=True)
    fk_service_type = models.ForeignKey('ServiceType', models.DO_NOTHING, db_column='fk_service_type')
    invoice_text = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'invoice'


class InvoiceCancellation(models.Model):
    id_cancellation = models.AutoField(primary_key=True)
    fk_invoice = models.ForeignKey(Invoice, models.DO_NOTHING, db_column='fk_invoice', blank=True, null=True)
    cancellation_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'invoice_cancellation'


class InvoiceStatus(models.Model):
    id_invoice_status = models.AutoField(primary_key=True)
    invoice_status = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'invoice_status'

    def __str__(self):
        return self.invoice_status

class OtherService(models.Model):
    id_other_service = models.AutoField(primary_key=True)
    fk_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='fk_customer')
    fk_currency = models.ForeignKey(Currency, models.DO_NOTHING, db_column='fk_currency')
    fk_unit = models.ForeignKey('Unit', models.DO_NOTHING, db_column='fk_unit')
    other_service_price = models.FloatField()
    other_service_description = models.CharField(max_length=1000)
    other_service_date = models.DateField()
    fk_invoice = models.ForeignKey(Invoice, models.DO_NOTHING, db_column='fk_invoice', blank=True, null=True)
    other_service_amount = models.FloatField()
    fk_service_clearing_type = models.ForeignKey('ServiceClearingType', models.DO_NOTHING, db_column='fk_service_clearing_type')
    fk_service_type = models.ForeignKey('ServiceType', models.DO_NOTHING, db_column='fk_service_type', blank=True, null=True)
    fk_service_status = models.ForeignKey('ServiceStatus', models.DO_NOTHING, db_column='fk_service_status', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'other_service'


class ServiceClearingType(models.Model):
    id_service_clearing_type = models.AutoField(primary_key=True)
    service_clearing_type = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'service_clearing_type'

    def __str__(self):
        return self.service_clearing_type

class ServiceStatus(models.Model):
    id_service_status = models.AutoField(primary_key=True)
    service_status = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'service_status'

    def __str__(self):
        return self.service_status

class ServiceType(models.Model):
    id_service_type = models.AutoField(primary_key=True)
    service_type = models.CharField(max_length=100, blank=True, null=True)
    service_type_vat = models.DecimalField(max_digits=5, decimal_places=3)
    service_type_model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'service_type'

    def __str__(self):
        return self.service_type

class Subcontractor(models.Model):
    id_subcontractor = models.AutoField(primary_key=True)
    subcontractor_company_name = models.CharField(max_length=100)
    subcontractor_residence = models.CharField(max_length=100)
    fk_township = models.ForeignKey('Township', models.DO_NOTHING, db_column='fk_township')
    subcontractor_email_contact = models.CharField(max_length=100)
    fk_sys_dimension_status = models.ForeignKey('SysDimensionStatus', models.DO_NOTHING, db_column='fk_sys_dimension_status', blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'subcontractor'

    def __str__(self):
        return self.subcontractor_company_name

class SysBug(models.Model):
    id_bug = models.AutoField(primary_key=True)
    bug_url = models.CharField(max_length=1000)
    bug_description = models.CharField(max_length=2000)
    fk_auth_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='fk_auth_user')
    fk_bug_status = models.ForeignKey('SysBugStatus', models.DO_NOTHING, db_column='fk_bug_status')
    fk_bug_priority = models.ForeignKey('SysBugPriority', models.DO_NOTHING, db_column='fk_bug_priority')

    class Meta:
        managed = True
        db_table = 'sys_bug'


class SysBugPriority(models.Model):
    id_bug_priority = models.IntegerField(primary_key=True)
    bug_priority = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sys_bug_priority'


class SysBugStatus(models.Model):
    id_bug_status = models.IntegerField(primary_key=True)
    bug_status = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'sys_bug_status'


class SysDimensionStatus(models.Model):
    id_sys_dimension_status = models.IntegerField(primary_key=True)
    dimension_status = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'sys_dimension_status'

    def __str__(self):
        return self.dimension_status

class Township(models.Model):
    id_township = models.AutoField(primary_key=True)
    township_zipcode = models.IntegerField()
    township_townname = models.CharField(max_length=100)
    township_country = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'township'

    def __str__(self):
        return str(self.township_zipcode) + ' - ' + self.township_townname

class Transportation(models.Model):
    id_transportation = models.AutoField(primary_key=True)
    fk_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='fk_customer')
    fk_service_status = models.ForeignKey(ServiceStatus, models.DO_NOTHING, db_column='fk_service_status')
    transportation_date_from = models.DateField(blank=True, null=True)
    transportation_date_to = models.DateField(blank=True, null=True)
    fk_currency = models.ForeignKey(Currency, models.DO_NOTHING, db_column='fk_currency', blank=True, null=True)
    transportation_amount = models.FloatField(blank=True, null=True)
    transportation_price = models.FloatField(blank=True, null=True)
    transportation_description = models.CharField(max_length=250, blank=True, null=True)
    fk_service_clearing_type = models.ForeignKey(ServiceClearingType, models.DO_NOTHING, db_column='fk_service_clearing_type', blank=True, null=True)
    fk_invoice = models.ForeignKey(Invoice, models.DO_NOTHING, db_column='fk_invoice', blank=True, null=True)
    fk_unit = models.ForeignKey('Unit', models.DO_NOTHING, db_column='fk_unit', blank=True, null=True)
    fk_vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING, related_name='related_vehicle', db_column='fk_vehicle', blank=True, null=True)
    fk_employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='fk_employee', blank=True, null=True)
    transportation_scan_file_path = models.CharField(max_length=2000, blank=True, null=True)
    transportation_customer_reference = models.CharField(max_length=100, blank=True, null=True)
    fk_subcontractor = models.ForeignKey(Subcontractor, models.DO_NOTHING, db_column='fk_subcontractor', blank=True, null=True)
    transportation_brokerage_fee = models.FloatField(blank=True, null=True)
    fk_vehicle_trailer = models.ForeignKey('Vehicle', models.DO_NOTHING, related_name='related_vehicle_trailer', db_column='fk_vehicle_trailer', blank=True, null=True)
    transportation_time_from = models.TimeField(blank=True, null=True)
    transportation_time_to = models.TimeField(blank=True, null=True)
    fk_service_type = models.ForeignKey(ServiceType, models.DO_NOTHING, db_column='fk_service_type', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'transportation'


class TransportationRoute(models.Model):
    id_transportation_route = models.AutoField(primary_key=True)
    fk_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='fk_customer')
    fk_currency = models.ForeignKey(Currency, models.DO_NOTHING, db_column='fk_currency')
    transportation_route_description = models.CharField(max_length=2000)
    fk_unit = models.ForeignKey('Unit', models.DO_NOTHING, db_column='fk_unit')
    transportation_route_price = models.FloatField()
    fk_service_type = models.ForeignKey(ServiceType, models.DO_NOTHING, db_column='fk_service_type')
    fk_service_clearing_type = models.ForeignKey(ServiceClearingType, models.DO_NOTHING, db_column='fk_service_clearing_type')

    class Meta:
        managed = True
        db_table = 'transportation_route'

    def __str__(self):
        return self.fk_customer.customer_internal_alias + ' - ' + self.transportation_route_description

class Unit(models.Model):
    unit_description = models.CharField(max_length=100)
    id_unit = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'unit'

    def __str__(self):
        return self.unit_description

class Vehicle(models.Model):
    vehicle_license_plate = models.CharField(max_length=100)
    fk_vehicle_type = models.ForeignKey('VehicleType', models.DO_NOTHING, db_column='fk_vehicle_type')
    id_vehicle = models.AutoField(primary_key=True)
    vehicle_internal_alias = models.CharField(unique=True, max_length=100)
    vehicle_first_registration = models.DateField(blank=True, null=True)
    vehicle_frame_number = models.CharField(max_length=100, blank=True, null=True)
    vehicle_description = models.CharField(max_length=100, blank=True, null=True)
    vehicle_max_loading_capacity = models.IntegerField(blank=True, null=True)
    vehicle_km_counter = models.IntegerField(blank=True, null=True)
    fk_sys_dimension_status = models.ForeignKey(SysDimensionStatus, models.DO_NOTHING, db_column='fk_sys_dimension_status', blank=True, null=True)
    fk_employee = models.ForeignKey('Employee', models.DO_NOTHING, db_column='fk_employee', unique=True, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'vehicle'

    def __str__(self):
        return self.vehicle_internal_alias

class VehicleAbsence(models.Model):
    id_vehicle_absence = models.AutoField(primary_key=True)
    vehicle_absence_date_from = models.DateField()
    vehicle_absence_date_to = models.DateField()
    vehicle_absence_time_from = models.TimeField(blank=True, null=True)
    vehicle_absence_time_to = models.TimeField(blank=True, null=True)
    fk_vehicle = models.ForeignKey(Vehicle, models.DO_NOTHING, db_column='fk_vehicle')
    fk_vehicle_absence_code = models.ForeignKey('VehicleAbsenceCode', models.DO_NOTHING, db_column='fk_vehicle_absence_code')

    class Meta:
        managed = True
        db_table = 'vehicle_absence'



class VehicleAbsenceCode(models.Model):
    id_vehicle_absence_code = models.AutoField(primary_key=True)
    vehicle_absence_code = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'vehicle_absence_code'

    def __str__(self):
        return self.vehicle_absence_code

class VehicleAllocation(models.Model):
    vehicle_allocation_date = models.DateField(primary_key=True)
    fk_vehicle = models.ForeignKey(Vehicle, models.DO_NOTHING, db_column='fk_vehicle')
    fk_employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='fk_employee', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vehicle_allocation'
        unique_together = (('vehicle_allocation_date', 'fk_vehicle'),)



class VehicleType(models.Model):
    id_vehicle_type = models.AutoField(primary_key=True)
    vehicle_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vehicle_type'

    def __str__(self):
        return self.vehicle_type
