from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import SysRecStates


class SysRecStatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SysRecStates
        fields = '__all__'