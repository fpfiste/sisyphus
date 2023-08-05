
from django.db import models


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