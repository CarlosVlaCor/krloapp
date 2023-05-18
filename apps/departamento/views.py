from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
# Create your views here.
from ..empleado.models import Empleado
from .models import Departamento


class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'departamento/lista.html'
    context_object_name = 'departamentos'


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        nombre = form.cleaned_data['name']
        apellido = form.cleaned_data['apellidos']
        depa = Departamento(
            nombre=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['short_name']
        )
        depa.save()
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa
        )
        return super(NewDepartamentoView, self).form_valid(form)
