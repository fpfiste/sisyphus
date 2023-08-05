from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import InvoiceStates


class InvoiceStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvoiceStates
        fields = '__all__'