from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import Sales


class SalesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'