from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView, DeleteView
)
# Create your views here.
from .models import Empleado
from .forms import EmpleadoForm


class InicioView(TemplateView):
    """ vista que carga la pagina de inicio """
    template_name = 'index.html'


class ListaAllEmpleados(ListView):
    template_name = 'empleado/list_all.html'
    paginate_by = 4
    context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        queryset = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return queryset


class ListaEmpleadosAdmin(ListView):
    template_name = 'empleado/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado


class ListByAreaEmpleado(ListView):
    template_name = 'empleado/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['short_name']
        queryset = Empleado.objects.filter(
            departamento__short_name=area
        )
        return queryset


class ListEmpleadoByKword(ListView):
    template_name = 'empleado/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        queryset = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return queryset


class ListHabilidadesEmpleado(ListView):
    template_name = 'empleado/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        habilidades = empleado.habilidades.all()
        return habilidades


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado/detail_empleado.html'

# 1 - Lista todos los empleados de la empresa
# 2 - Listar todos los empleados que pertenecen al area de la empresa
# 3 - Listar empleados por palabra clave
# 4 - Listar habilidades de un empleado


class SuccesView(TemplateView):
    template_name = 'empleado/succes.html'


# Nambre, hasta se crea el html
class EmpleadoCreateView(CreateView):
    template_name = "empleado/add.html"
    model = Empleado
    form_class = EmpleadoForm
    # success_url = '.'  Redirije a la misma pagina
    success_url = reverse_lazy('empleado_app:empleados_admin')

    def form_valid(self, form):
        # Logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = 'empleado/update.html'
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades'
    ]
    success_url = reverse_lazy('empleado_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('**************METODO POST***************')
        print('===============================================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # Logica del proceso
        print('**************METODO Form valida***************')

        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleado/delete.html'
    success_url = reverse_lazy('empleado_app:empleados_admin')
