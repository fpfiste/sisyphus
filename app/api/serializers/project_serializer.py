from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import Projects


class ProjectsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'