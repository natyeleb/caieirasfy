# Create your tests here.
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from artista.models import Artista
from landing.serializers import ArtistaSerializer


class ArtistaViewSet(viewsets.ModelViewSet):
    filter_backends = SearchFilter
    search_fields = ['^nome', '^idade', '^estilo_musical']
    queryset = Artista.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ArtistaSerializer
