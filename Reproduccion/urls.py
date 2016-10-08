from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^editar/(?P<pk>\d+)$', views.EditarReproduccion.as_view(), name='editar'),
    url(r'^nuevo/$', views.CrearReproduccion.as_view(), name='nuevo'),
    url(r'^buscar/(?P<pk>\d+)$', views.BuscarReproduccion.as_view(), name='buscar'),
    url(r'^listar/$', views.ListarReproducciones.as_view(), name='listar'),
    #url(r'^', views..as_view(), name='usuario'),
]
