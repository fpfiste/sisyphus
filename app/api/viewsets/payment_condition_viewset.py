from rest_framework import viewsets

from api.components import PaymentConditions, PaymentConditionSerializer



class PaymentConditionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PaymentConditions.objects.all()
    serializer_class = PaymentConditionSerializer