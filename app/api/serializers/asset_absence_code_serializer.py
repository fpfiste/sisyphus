from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import AssetAbsenceCodes


class AssetAbsenceCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AssetAbsenceCodes
        fields = '__all__'