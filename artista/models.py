from django.db import models

# Create your models here.
class Artista(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name='None'
    )
    idade = models.CharField(
        max_length=50,
        verbose_name='Idade'
    )
    estilos_musicais = models.CharField(
        max_length=50,
        verbose_name= 'Estilo musicais'
    )

    def __str__(self):
        return self.nome + ' ' + self.artista