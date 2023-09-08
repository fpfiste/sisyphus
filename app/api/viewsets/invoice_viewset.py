from rest_framework import viewsets

from api.components import Invoices, InvoiceSerializer



class InvoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Invoices.objects.all()
    serializer_class = InvoiceSerializer


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Invoices.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != ''])
        data = queryset.filter(**params)
        return data
