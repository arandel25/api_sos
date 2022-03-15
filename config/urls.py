
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from endereco.views import EnderecoViewSet
from local.views import LocalViewSet

router = routers.SimpleRouter()
router.register('enderecos', EnderecoViewSet)
router.register('locais', LocalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("v1/", include(router.urls)),
]
