from rest_framework import viewsets

from api.models import PaymentConditions
from api.serializers import PaymentConditionSerializer


class PaymentConditionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PaymentConditions.objects.all()
    serializer_class = PaymentConditionSerializer