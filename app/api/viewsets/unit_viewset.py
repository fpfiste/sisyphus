from rest_framework import viewsets

from api.models import Units
from api.serializers import UnitSerializer


class UnitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Units.objects.all()
    serializer_class = UnitSerializer