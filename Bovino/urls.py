from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^editar/(?P<pk>\d+)$', views.EditarBovino.as_view(), name='editar'),
    url(r'^nuevo/$', views.CrearBovino.as_view(), name='nuevo'),
    url(r'^buscar/(?P<pk>\d+)$', views.BuscarBovino.as_view(), name='buscar'),
    url(r'^listar/$', views.ListarBovino.as_view(), name='listar'),
    #url(r'^', views..as_view(), name='usuario'),
]
