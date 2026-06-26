from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Estudiante

class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'estudiante/list.html'
    context_object_name = 'estudiante' 

class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = '__all__'
    template_name = 'estudiante/create.html'
    success_url = reverse_lazy('estudiante:estudiante_list')

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = '__all__'
    template_name = 'estudiante/update.html'
    success_url = reverse_lazy('estudiante:estudiante_list')

class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = 'estudiante/delete.html'
    success_url = reverse_lazy('estudiante:estudiante_list')