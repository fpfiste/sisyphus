from rest_framework import viewsets

from api.components import AssetTaskAllocation, AssetTaskAllocationSerializer



class AssetTaskAllocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AssetTaskAllocation.objects.all()
    serializer_class = AssetTaskAllocationSerializer
