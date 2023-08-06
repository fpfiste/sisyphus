from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import Units


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Units
        fields = '__all__'