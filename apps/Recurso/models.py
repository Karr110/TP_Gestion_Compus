from django.db import models

class Recurso(models.Model):
    marca_computadora = models.CharField(max_length=100, default='Lenovo')
    numero_equipo = models.CharField(max_length=50)
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca_computadora} N°{self.numero_equipo}"
