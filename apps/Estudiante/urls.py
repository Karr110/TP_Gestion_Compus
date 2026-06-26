from django.urls import path
from .views import EstudianteListView, EstudianteCreateView, EstudianteUpdateView, EstudianteDeleteView

app_name = "estudiantes"

urlpatterns = [
    path('', EstudianteListView.as_view(), name='estudiante_list'),
    path('nuevo/', EstudianteCreateView.as_view(), name='estudiante_create'),
    path('<int:pk>/editar/', EstudianteUpdateView.as_view(), name='estudiante_update'),
    path('<int:pk>/eliminar/', EstudianteDeleteView.as_view(), name='estudiante_delete')
]