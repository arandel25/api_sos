from rest_framework import viewsets
from endereco.models import Endereco
from endereco.serializers import EnderecoSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    serializer_class = EnderecoSerializer
    queryset = Endereco.objects.all()
    http_method_names = ['get', "post", "patch"]

 


