from django.urls import path
from .views import RecursoListView, RecursoCreateView, RecursoUpdateView, RecursoDeleteView

app_name = "recursos"

urlpatterns = [
    path('', RecursoListView.as_view(), name='recurso_list'),
    path('nuevo/', RecursoCreateView.as_view(), name='recurso_create'),
    path('<int:pk>/editar/', RecursoUpdateView.as_view(), name='recurso_update'),
    path('<int:pk>/eliminar/', RecursoDeleteView.as_view(), name='recurso_delete')
]