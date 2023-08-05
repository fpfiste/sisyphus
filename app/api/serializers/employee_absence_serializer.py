from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import EmployeeAbsences


class EmployeeAbsenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeAbsences
        fields = '__all__'