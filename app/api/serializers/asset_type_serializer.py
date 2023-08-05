from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import AssetTypes


class AssetTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AssetTypes
        fields = '__all__'