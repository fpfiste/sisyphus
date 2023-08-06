from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import TaskStates


class TaskStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskStates
        fields = '__all__'