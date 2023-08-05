from rest_framework import viewsets

from api.models import Assets
from api.serializers import AssetSerializer


class AssetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Assets.objects.all()
    serializer_class = AssetSerializer
