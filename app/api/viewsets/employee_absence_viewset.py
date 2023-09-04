from rest_framework import viewsets
from api.components import EmployeeAbsences, EmployeeAbsenceSerializer


class EmployeeAbsenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EmployeeAbsences.objects.all()
    serializer_class = EmployeeAbsenceSerializer
