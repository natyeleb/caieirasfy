from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from landing.models import Musica
from landing.serializers import MusicaSerializer



class MusicaViewSet(viewsets.ModelViewSet):
    filter_backends = (SearchFilter,)
    search_fields = ['^nome', '^artista', '^genero_musical', '^link']
    queryset = Musica.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = MusicaSerializer
