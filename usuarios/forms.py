from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth. models import User

class FormularioRegistro(UserCreationForm):
    username =  forms.CharField(label="Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        helps_text = {llave : "" for llave in fields}

class FormularioEditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    sports = forms.CharField(label="Deportes")
    hobbies = forms.CharField(label="Hobbies")
    avatar = forms.ImageField(required=False)
    
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "sports", "hobbies", "avatar"]