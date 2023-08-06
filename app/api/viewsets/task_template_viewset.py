from rest_framework import viewsets

from api.models import TaskTemplates
from api.serializers import TaskTemplateSerializer


class TaskTemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TaskTemplates.objects.all()
    serializer_class = TaskTemplateSerializer