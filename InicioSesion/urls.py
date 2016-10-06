from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^salir/$', auth_views.logout, {'next_page':'/'}, name='salir'),
    url(r'^inicio/$', views.hello, name='hello'),
    url(r'^', views.InicioSesionView.as_view(), name='autenticar'),
]
