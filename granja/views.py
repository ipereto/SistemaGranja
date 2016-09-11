from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Granja

# Create your views here.
def hello_world(request):
    #return HttpResponse('Hello world!')
    #return render(request, 'index.html')
    granja = Granja.objects.order_by('id')
    template = loader.get_template('index.html')
    context = {
    'granja' : granja
    }
    return HttpResponse(template.render(context,request))
