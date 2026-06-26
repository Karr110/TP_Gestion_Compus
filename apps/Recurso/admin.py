from django.contrib import admin
from .models import Recurso

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    #list_display = ('tipo_computadora','numero_equipo', 'disponibilidad')
    list_display = ('numero_equipo', 'disponibilidad')
    list_filter = ('disponibilidad',)