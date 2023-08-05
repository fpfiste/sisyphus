from rest_framework import viewsets

from api.models import Projects
from api.serializers import ProjectsSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer