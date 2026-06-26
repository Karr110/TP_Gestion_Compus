from django.urls import path
from .views import ReservaListView, ReservaCreateView, ReservaUpdateView, ReservaDeleteView

app_name = "reservas"

urlpatterns = [
    path('', ReservaListView.as_view(), name='reserva_list'),
    path('nuevo/', ReservaCreateView.as_view(), name='reserva_create'),
    path('<int:pk>/editar/', ReservaUpdateView.as_view(), name='reserva_update'),
    path('<int:pk>/eliminar/', ReservaDeleteView.as_view(), name='reserva_delete')
]