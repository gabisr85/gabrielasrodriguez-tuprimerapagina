from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login as django_login
from usuarios.forms import FormularioRegistro, FormularioEditarPerfil
from django.contrib.auth.decorators import login_required
from usuarios.models import InfoExtra


def login(request):
    if request.method== "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            django_login(request, usuario)

            InfoExtra.objects.get_or_create(user=usuario)

            return redirect("inicio")
    else:
        formulario = AuthenticationForm()
    return render(request, "usuarios/login.html", {'formulario' : formulario}) 

def registro(request):
    if request.method == "POST":
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():

            formulario.save()

            return redirect("login")
    else:
        formulario = FormularioRegistro()
        
    return render(request, "usuarios/registro.html", {'formulario' : formulario})

@login_required
def editar_perfil(request):

    infoextra = request.user.infoextra
    if request.method == "POST":
        formulario = FormularioEditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            infoextra.sports = formulario.cleaned_data.get('sports')
            infoextra.hobbies = formulario.cleaned_data.get('hobbies')

            if formulario.cleaned_data.get('avatar'):
                infoextra.avatar = formulario.cleaned_data.get('avatar')

            infoextra.save()                     

            formulario.save()

            return redirect("login")
    else:
        formulario = FormularioEditarPerfil(initial={'sports' : infoextra.sports, 'hobbies' : infoextra.hobbies, 'avatar' : infoextra.avatar}, instance=request.user)
        
    return render(request, "usuarios/editar_perfil.html", {'formulario' : formulario})

@login_required
def perfil_usuario(request):
    info_extra  = request.user.infoextra
    context = {'usuario' : request.user, 'info_extra' : info_extra}
    return render(request, "usuarios/perfil.html", context)