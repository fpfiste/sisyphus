from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import PaymentConditions


class PaymentConditionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentConditions
        fields = '__all__'