from rest_framework import viewsets

from api.components import EmployeeAbsenceCodes, EmployeeAbsenceCodeSerializer



class EmployeeAbsenceCodesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EmployeeAbsenceCodes.objects.all()
    serializer_class = EmployeeAbsenceCodeSerializer
