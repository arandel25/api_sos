from dataclasses import field
from rest_framework import serializers
from local.models import Local
from endereco.serializers import EnderecoSerializer

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        exclude = ("modified", "created")

class LocalSerializerRetrieve(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    class Meta:
        model = Local
        fields = ("tipo", "titulo", "numero", "endereco")