from rest_framework import viewsets

from api.components import AssetTypes
from api.components import AssetTypeSerializer


class AssetTypesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AssetTypes.objects.all()
    serializer_class = AssetTypeSerializer
