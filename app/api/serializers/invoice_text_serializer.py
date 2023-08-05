from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import InvoiceTexts


class InvoiceTextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvoiceTexts
        fields = '__all__'