from rest_framework import viewsets

from api.components import EmployeeTaskAllocation, EmployeeTaskAllocationSerializer



class EmployeeTaskAllocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EmployeeTaskAllocation.objects.all()
    serializer_class = EmployeeTaskAllocationSerializer