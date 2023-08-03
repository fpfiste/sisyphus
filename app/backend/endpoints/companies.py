from django.db import models
from rest_framework import serializers, viewsets, permissions


class Company(models.Model):
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

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fiels = [__all__]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Company.objects.all().order_by('id_company')
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]