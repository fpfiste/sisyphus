from rest_framework import viewsets

from api.components import SysRecStates, SysRecStatesSerializer


class SysRecStateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SysRecStates.objects.all()
    serializer_class = SysRecStatesSerializer


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = SysRecStates.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != ''])
        data = queryset.filter(**params)
        return data
