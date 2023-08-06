from rest_framework import viewsets

from api.models import TaskStates
from api.serializers import TaskStateSerializer


class TaskStateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TaskStates.objects.all()
    serializer_class = TaskStateSerializer