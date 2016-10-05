from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def autenticar(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        usuario = request.POST.get('usuario', None)
        clave = request.POST.get('clave', None)

        if action == 'registrar':
            user = User.objects.create_user(username=usuario,password=clave)
            user.save()
        elif action == 'login':
            user = authenticate(username=usuario, password=clave)
            login(request, user)
        return redirect('/')

    return render(request, 'login/login.html', {})

def hello(request):
    return render(request,'hello.html',{})
