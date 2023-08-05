from rest_framework import viewsets

from api.models import EmployeeTypes
from api.serializers import EmployeeTypeSerializer


class EmployeeTypesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EmployeeTypes.objects.all()
    serializer_class = EmployeeTypeSerializer
