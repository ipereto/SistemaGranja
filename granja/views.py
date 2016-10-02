from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.template import loader

# Class-Based views
from django.views.generic import ListView

from .forms import GranjaForm

from .models import Granja

# Create your views here.

def granja_detail(request, pk):
    granja = get_object_or_404(Granja, pk=pk)
    template = loader.get_template('granja_detail.html')
    context = {
    'granja' : granja
    }
    return HttpResponse(template.render(context, request))

#Implementacion de un formulario
def new_granja(request):
    if request.method == 'POST':
        form = GranjaForm(request.POST, request.FILES)
        if form.is_valid():
            granja = form.save()
            granja.save()
            return HttpResponseRedirect('/')
    else:
        form = GranjaForm()

    template = loader.get_template('new_granja.html')
    context = {
        'form' : form
    }
    return HttpResponse(template.render(context, request))

class ListarGranja(ListView):
    model = Granja
