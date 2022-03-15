from django.db import models
from django_extensions.db.models import TimeStampedModel

class Endereco (TimeStampedModel):

    logradouro = models.CharField(
        db_column="LOGRADOURO", 
        max_length=100,
    )

    cep = models.CharField(
        db_column="CEP",
        max_length=9,
    )
    
    bairro = models.CharField(
        db_column="BAIRRO",
        max_length=25,
    )

    cidade = models.CharField(
        db_column="CIDADE",
        max_length=30,
    )

    uf = models.CharField(
        db_column="UF", 
        max_length=2,

    )

    class Meta:
        db_table="ENDERECO"
        verbose_name = "endereco"
        verbose_name_plural = "enderecos"


 
