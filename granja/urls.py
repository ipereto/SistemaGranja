from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.hello_world, name='hello'),
    url(r'^$', views.ListarGranja.as_view(), name='hello'),
    url(r'^granja/(?P<pk>[0-9]+)/$', views.granja_detail),
    url(r'^granja/new', views.new_granja, name='new_granja')
]
