from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import Currencies


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currencies
        fields = '__all__'