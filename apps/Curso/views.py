from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Curso

class CursoListView(ListView):
    model = Curso
    template_name = 'cursos/list.html'
    context_object_name = 'cursos' 

class CursoCreateView(CreateView):
    model = Curso
    fields = '__all__'
    template_name = 'cursos/create.html'
    success_url = reverse_lazy('cursos:curso_list')

class CursoUpdateView(UpdateView):
    model = Curso
    fields = '__all__'
    template_name = 'cursos/update.html'
    success_url = reverse_lazy('cursos:curso_list')

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'cursos/delete.html'
    success_url = reverse_lazy('cursos:curso_list')