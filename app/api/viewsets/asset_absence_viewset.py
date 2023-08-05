from rest_framework import viewsets

from api.models import AssetAbsences
from api.serializers import AssetAbsenceSerializer


class AssetAbsenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AssetAbsences.objects.all()
    serializer_class = AssetAbsenceSerializer
