from tabnanny import verbose
from django.db import models
from django_extensions.db.models import TimeStampedModel
from endereco.models import Endereco

class Local(TimeStampedModel):
    tipo = models.CharField(max_length=100, db_column="tipo")
    titulo = models.CharField(max_length=80, db_column="titulo")
    numero = models.CharField(max_length=80, db_column="numero")
    endereco = models.OneToOneField(
        to=Endereco, on_delete=models.DO_NOTHING, db_column="endereco"
    )

    class Meta:
        db_table = "local"
        verbose_name = "local"
        verbose_name_plural = "locais"