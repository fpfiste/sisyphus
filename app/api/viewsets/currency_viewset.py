from rest_framework import viewsets

from api.models import Currencies
from api.serializers import CurrencySerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Currencies.objects.all()
    serializer_class = CurrencySerializer
