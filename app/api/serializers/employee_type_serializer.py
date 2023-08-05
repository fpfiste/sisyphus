from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import EmployeeTypes


class EmployeeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeTypes
        fields = '__all__'