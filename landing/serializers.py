from rest_framework import serializers

from artista.models import Artista
from .models import Musica

class MusicaSerializer(serializers.Serializer):
    nome = serializers.CharField(read_only=True)
    tempo_reproducao = serializers.CharField()
    artista = serializers.CharField()
    genero_musical = serializers.CharField()

    def create(self, validated_data):
        musica = Musica.objects.create(**validated_data)
        return musica

class ArtistaSerializer(serializers.Serializer):
    nome = serializers.IntegerField(read_only=True)
    idade = serializers.CharField(read_only=True)
    estilos_musicais = serializers.CharField(read_only=True)

    def create(self, validated_data):
        artista = Artista.objects.create(**validated_data)
        return artista



    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.tempo_reproducao = validated_data('tempo de reproduçao')
        instance.artista = validated_data.get('artista')
        instance.genero = validated_data.get('genero')
        instance.save()
        return instance