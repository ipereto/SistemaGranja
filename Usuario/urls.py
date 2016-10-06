from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^editar/$', views.EditarUsuario.as_view(), name='editar'),
    url(r'^nuevo/$', views.CrearUsuario.as_view(), name='nuevo'),
    url(r'^buscar/$', views.BuscarUsuario.as_view(), name='buscar'),
    url(r'^listar/$', views.ListarUsuarios.as_view(), name='listar'),
    url(r'^', views.UsuarioView.as_view(), name='usuario'),
]
