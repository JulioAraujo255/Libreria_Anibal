from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    puntaje = models.IntegerField()  # por ejemplo: 1 a 5
    comentario = models.TextField(blank=True)

    def __str__(self):
        return f"{self.puntaje} estrellas"

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)
    calificacion = models.ForeignKey(Calificacion, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
