from rest_framework import viewsets

from api.models import Invoices
from api.serializers import InvoiceSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Invoices.objects.all()
    serializer_class = InvoiceSerializer