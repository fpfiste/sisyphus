from rest_framework import viewsets

from api.models import Sales
from api.serializers import SalesSerializer


class SalesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer