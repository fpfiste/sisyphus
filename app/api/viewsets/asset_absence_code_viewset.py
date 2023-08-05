from rest_framework import viewsets

from api.models import AssetAbsenceCodes
from api.serializers import AssetAbsenceCodeSerializer


class AssetAbsenceCodesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AssetAbsenceCodes.objects.all()
    serializer_class = AssetAbsenceCodeSerializer
