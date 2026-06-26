from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'recurso', 'fecha_hr_prestamo', 'estado_prestamo')
    list_filter = ('estado_prestamo', 'curso',)