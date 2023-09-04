from rest_framework import viewsets, permissions

from api.components import AssetAbsenceCodes
from api.components import AssetAbsenceCodeSerializer


class AssetAbsenceCodesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AssetAbsenceCodes.objects.all()
    serializer_class = AssetAbsenceCodeSerializer
    permission_classes = [permissions.IsAuthenticated]
