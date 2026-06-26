from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Recurso

class RecursoListView(ListView):
    model = Recurso
    template_name = 'recurso/list.html'
    context_object_name = 'recurso' 

class RecursoCreateView(CreateView):
    model = Recurso
    fields = '__all__'
    template_name = 'recurso/create.html'
    success_url = reverse_lazy('recurso:recurso_list')

class RecursoUpdateView(UpdateView):
    model = Recurso
    fields = '__all__'
    template_name = 'recurso/update.html'
    success_url = reverse_lazy('recurso:recurso_list')

class RecursoDeleteView(DeleteView):
    model = Recurso
    template_name = 'recurso/delete.html'
    success_url = reverse_lazy('recurso:recurso_list')