from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^editar/(?P<pk>\d+)$', views.Editarespacio.as_view(), name='editar'),
    url(r'^nuevo/$', views.Crearespacio.as_view(), name='nuevo'),
    url(r'^buscar/(?P<pk>\d+)$', views.Buscarespacio.as_view(), name='buscar'),
    url(r'^listar/$', views.Listarespacio.as_view(), name='listar'),
    url(r'^', views.espacioView.as_view(), name='Espacio'),
]
