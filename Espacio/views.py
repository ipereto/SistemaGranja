# Create your views here.
# from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login

# Create your views here.
# def autenticar(request):
#     if request.method == 'POST':
#         action = request.POST.get('action', None)
#         usuario = request.POST.get('usuario', None)
#         clave = request.POST.get('clave', None)
#
#         if action == 'registrar':
#             user = User.objects.create_user(username=usuario,password=clave)
#             user.save()
#         elif action == 'login':
#             user = authenticate(username=usuario, password=clave)
#             login(request, user)
#         return redirect('/')
#
#     return render(request, 'login/login.html', {})

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
from .forms import CreacionUsuarioForm
from django.contrib.auth.models import Group
from InicioSesion.mixins import JSONResponseMixin
from InicioSesion.mixins import LoginRequiredMixin


class espacioView(LoginRequiredMixin, TemplateView):
    template_name = 'espacios/espacio.html'
    def get_context_data(self, **kwargs):
        context = super(espacioView, self).get_context_data(**kwargs)
        context.update({'form': CreacionespacioForm()})
        return context

class Crearespacio(LoginRequiredMixin, CreateView):
    model = Espacio
    success_url = reverse_lazy('Espacio:listar')
    fields = ['espacio','Estado','granja','tipo','area','capacidad','nombre','aforo','porcentaje_desperdicio']

class Listarespacio(LoginRequiredMixin, ListView):
    model = Espacio
    # template_name = 'user_list.html'
    # paginate_by = 5

class Editarespacio(LoginRequiredMixin, UpdateView):
    model = Espacio
    form_class = CreacionespacioForm
    #success_url =

class Buscarespacio(LoginRequiredMixin, JSONResponseMixin, DetailView):
    model = Espacio
    # slug_field = 'username'
    # slug_url_kwarg = 'username'
    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     return self.render_to_json_response()
    # def get_data(self):
    #     data = {
    #         'usuario':{
    #             'username': self.object.username,
    #             'first_name': self.object.first_name,
    #             'last_name': self.object.last_name,
    #             'is_superuser': self.object.is_superuser,
    #             'is_active': self.object.is_active
    #         }
    #     }
    #     return data
