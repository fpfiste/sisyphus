from rest_framework import viewsets

from api.models import SysRecStates
from api.serializers import SysRecStatesSerializer


class SysRecStateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SysRecStates.objects.all()
    serializer_class = SysRecStatesSerializer