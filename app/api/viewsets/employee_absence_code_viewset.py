from rest_framework import viewsets

from api.models import EmployeeAbsenceCodes
from api.serializers import EmployeeAbsenceCodeSerializer


class EmployeeAbsenceCodesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EmployeeAbsenceCodes.objects.all()
    serializer_class = EmployeeAbsenceCodeSerializer
