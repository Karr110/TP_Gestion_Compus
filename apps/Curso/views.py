from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Curso

class CursoListView(ListView):
    model = Curso
    template_name = 'curso/list.html'
    context_object_name = 'cursos' 

class CursoCreateView(CreateView):
    model = Curso
    fields = '__all__'
    template_name = 'curso/create.html'
    success_url = reverse_lazy('curso:curso_list')

class CursoUpdateView(UpdateView):
    model = Curso
    fields = '__all__'
    template_name = 'curso/update.html'
    success_url = reverse_lazy('curso:curso_list')

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'curso/delete.html'
    success_url = reverse_lazy('curso:curso_list')