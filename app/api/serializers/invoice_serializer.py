from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import Invoices


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoices
        fields = '__all__'