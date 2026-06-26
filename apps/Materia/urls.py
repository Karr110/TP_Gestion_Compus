from django.urls import path
from .views import MateriaListView, MateriaCreateView, MateriaUpdateView, MateriaDeleteView

app_name = "materias"

urlpatterns = [
    path('', MateriaListView.as_view(), name='materia_list'),
    path('nuevo/', MateriaCreateView.as_view(), name='materia_create'),
    path('<int:pk>/editar/', MateriaUpdateView.as_view(), name='materia_update'),
    path('<int:pk>/eliminar/', MateriaDeleteView.as_view(), name='materia_delete')
]