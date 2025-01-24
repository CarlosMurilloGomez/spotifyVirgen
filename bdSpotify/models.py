from datetime import datetime, timedelta

from django.db import models

# Create your models here.

class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    es_activo = models.BooleanField(default=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="listas")

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(fecha_nacimiento__lte=datetime.today()-timedelta(days=365*18)), name="ch_edad_gte_18")
        ]

    def __str__(self):
        return f'ID:{self.id} - Email: {self.email}'

class Genero(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Album(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} - {self.nombre}'

class Cancion(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    duracion = models.IntegerField()
    fecha_lanzamiento = models.DateField()

    def __str__(self):
        return f"ID:{self.id} - {self.titulo} de {self.artista}"

class Lista(models.Model):
    nombre = models.CharField(max_length=200)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateField()

    def __str__(self):
        return f"{self.nombre} de {self.usuario.email}"

class ListaCancion(models.Model):
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["cancion", "lista"], name="clave_secundaria")
        ]

    def __str__(self):
        return f"Lista: {self.lista.nombre} - Cancion: {self.cancion.titulo}"
