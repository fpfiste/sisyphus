from rest_framework import viewsets

from api.components import Invoices, InvoiceSerializer



class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Invoices.objects.all()
    serializer_class = InvoiceSerializer