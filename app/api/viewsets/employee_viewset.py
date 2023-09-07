from rest_framework import viewsets

from api.components import Employees, EmployeeSerializer



class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Employees.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != ''])
        print(params)
        data = queryset.filter(**params)
        print(data)
        return data