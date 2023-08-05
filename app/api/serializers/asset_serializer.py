from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import Assets


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assets
        fields = '__all__'