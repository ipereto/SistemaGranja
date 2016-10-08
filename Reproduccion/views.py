from django.shortcuts import render
from django.template import loader
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    JsonResponse,
)
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.template import loader
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ReproduccionForm
from django.contrib.auth.models import Group
from InicioSesion.mixins import JSONResponseMixin
from InicioSesion.mixins import LoginRequiredMixin
from .models import Reproduccion

class ReproduccionView(LoginRequiredMixin, TemplateView):
    template_name = 'Reproduccion/reproduccion_form.html'
    def get_context_data(self, **kwargs):
        context = super(UsuarioView, self).get_context_data(**kwargs)
        context.update({'form': ReproduccionForm()})
        return context

class CrearReproduccion(LoginRequiredMixin, CreateView):
    model = Reproduccion
    success_url = reverse_lazy('reproducciones:listar')
    fields = ['id_bovino', 'id_toro', 'id_servicio', 'id_cria',
              'id_semen_toro', 'fecha_servicio', 'proximoCelo',
              'fechaPosibleParto','cantCelosPosParto',
              'fechaSecado','id_estado']

class ListarReproducciones(LoginRequiredMixin, ListView):
    model = Reproduccion
    template_name = 'Reproduccion/reproduccion_list.html'
    # paginate_by = 5

class EditarReproduccion(LoginRequiredMixin, UpdateView):
    model = Reproduccion
    form_class = ReproduccionForm
    #success_url =

class BuscarReproduccion(LoginRequiredMixin, JSONResponseMixin, DetailView):
    model = Reproduccion
