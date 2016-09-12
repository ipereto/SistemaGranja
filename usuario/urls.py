from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login$', views.autenticar, name='autenticar'),
    url(r'^', views.hello, name='hello'),
    url(r'^salir$', auth_views.logout, {'next_page':'/'}, name='salir'),
]
