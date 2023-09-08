from rest_framework import viewsets
from api.components import Units, UnitSerializer



class UnitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Units.objects.all()
    serializer_class = UnitSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Units.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != ''])
        data = queryset.filter(**params)
        return data
