from rest_framework import viewsets

from api.components import InvoiceTexts, InvoiceTextSerializer



class InvoiceTextViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = InvoiceTexts.objects.all()
    serializer_class = InvoiceTextSerializer
