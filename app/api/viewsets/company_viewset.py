from rest_framework import viewsets

from api.models import Companies
from api.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer
