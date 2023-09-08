from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from urllib.parse import urlparse
from api.components import Tasks, TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Tasks.objects.all()

        params = dict([(key,value) for key, value in self.request.query_params.items() if value != ''])

        data = queryset.filter(**params)


        return data


