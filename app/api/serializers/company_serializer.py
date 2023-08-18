from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import Companies


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = '__all__'