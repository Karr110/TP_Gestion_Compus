from django.db import models
from apps.Curso.models import Curso

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.curso})"