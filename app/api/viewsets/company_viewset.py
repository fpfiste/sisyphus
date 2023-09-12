from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.components import Companies, CompanySerializer



class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Companies.objects.all()

        params = dict([(key,value) for key, value in self.request.query_params.items() if value != ''])

        data = queryset.filter(**params).order_by('-id_company')

        return data

