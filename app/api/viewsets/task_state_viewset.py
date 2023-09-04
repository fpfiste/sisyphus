from rest_framework import viewsets

from api.components import TaskStates, TaskStateSerializer



class TaskStateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TaskStates.objects.all()
    serializer_class = TaskStateSerializer