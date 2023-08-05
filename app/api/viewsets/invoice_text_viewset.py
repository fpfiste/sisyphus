from rest_framework import viewsets

from api.models import InvoiceTexts
from api.serializers import InvoiceTextSerializer


class InvoiceTextViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = InvoiceTexts.objects.all()
    serializer_class = InvoiceTextSerializer
