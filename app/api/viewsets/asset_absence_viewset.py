from rest_framework import viewsets

from api.components import AssetAbsences
from api.components import AssetAbsenceSerializer


class AssetAbsenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AssetAbsences.objects.all()
    serializer_class = AssetAbsenceSerializer
