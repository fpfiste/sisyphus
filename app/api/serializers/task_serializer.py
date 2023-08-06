from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import Tasks


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'