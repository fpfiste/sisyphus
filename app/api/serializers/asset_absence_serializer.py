from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import AssetAbsences


class AssetAbsenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AssetAbsences
        fields = '__all__'