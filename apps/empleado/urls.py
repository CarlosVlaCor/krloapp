from django.urls import path
from . import views

app_name = 'empleado_app'
urlpatterns = [
    path('',
         views.InicioView.as_view(),
         name='inicio'),
    path(
        'listarAllEmpleados/',
        views.ListaAllEmpleados.as_view(),
        name='empleados_all'
    ),
    path('list-by-area/<short_name>/',
         views.ListByAreaEmpleado.as_view(),
         name='empleados_area'),
    path('lista-empleados-admin/',
         views.ListaEmpleadosAdmin.as_view(),
         name='empleados_admin'),
    path('buscar-empleado/', views.ListEmpleadoByKword.as_view()),
    path('habilidades/', views.ListHabilidadesEmpleado.as_view()),
    path(
        'ver_empleado/<pk>/',
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'
    ),
    path(
        'add_empleado/',
        views.EmpleadoCreateView.as_view(),
        name='empleado_add'),
    path('succes/', views.SuccesView.as_view(), name='correcto'),
    path(
        'update_empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'),
    path('delete-empleado/<pk>/',
         views.EmpleadoDeleteView.as_view(),
         name='eliminar_empleado')
]

