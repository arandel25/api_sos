from rest_framework import viewsets
from local.models import Local
from local.serializers import LocalSerializer, LocalSerializerRetrieve
from rest_framework.response import Response

class LocalViewSet(viewsets.ModelViewSet):
    serializer_class = LocalSerializer
    serializer_list_retrive = LocalSerializerRetrieve
    queryset = Local.objects.all()
    http_method_names = ["get", "post", "patch"]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_list_retrive(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_list_retrive(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_list_retrive(instance)
        return Response(serializer.data)