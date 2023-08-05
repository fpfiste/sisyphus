from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import Employees


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'