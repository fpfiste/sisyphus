from rest_framework import viewsets

from api.models import InvoiceStates
from api.serializers import InvoiceStateSerializer


class InvoiceStateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = InvoiceStates.objects.all()
    serializer_class = InvoiceStateSerializer
