from rest_framework import viewsets, permissions

from api.components import AssetAbsenceCodes
from api.components import AssetAbsenceCodeSerializer


class AssetAbsenceCodesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AssetAbsenceCodes.objects.all()
    serializer_class = AssetAbsenceCodeSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = AssetAbsenceCodes.objects.all()
        params = dict([(key,value) for key, value in self.request.query_params.items() if value != ''])
        print(params)
        data = queryset.filter(**params)
        print(data)
        return data
