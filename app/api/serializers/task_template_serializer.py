from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import TaskTemplates


class TaskTemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskTemplates
        fields = '__all__'