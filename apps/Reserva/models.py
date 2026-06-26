from django.db import models
from apps.Curso.models import Curso
from apps.Estudiante.models import Estudiante
from apps.Materia.models import Materia
from apps.Recurso.models import Recurso

class Reserva(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE )
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE )
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE )
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE )
    fecha_hr_prestamo = models.DateTimeField(auto_now_add=True)
    estado_prestamo = models.CharField(max_length=50, default='Activa')

    def __str__(self):
        return f"Reserva de {self.estudiante.apellido} - {self.recurso}"