from rest_framework import viewsets

from api.models import Employees
from api.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
