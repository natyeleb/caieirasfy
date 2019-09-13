from django.db import models


# Create your models here.

class Musica(models.Model):
   nome = models.CharField(
        max_length=50,
        verbose_name='Nome'
    )
   tempo_reproducao = models.CharField(
        max_length=50,
        verbose_name='Tempo de reprodução'
    )
   artista = models.CharField(
        max_length=50,
        verbose_name='Artista'
    )
   genero_musical = models.CharField(
       max_length=255,
       verbose_name='Genero musical'
   )

   def __str__(self):
       return self.nome + ' ' + self.artista

