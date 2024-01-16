from django.db import models

# Create your models here.
class Deportista(models.Model):
    name = models.CharField(max_length = 200) #Nombre
    age = models.IntegerField()
    genero = models.CharField(max_length = 20)
    Puntos = models.IntegerField()
    Wins = models.IntegerField()
    Losses = models.IntegerField()
    Diff = models.IntegerField()

    def __str__(self):
        return self.name

