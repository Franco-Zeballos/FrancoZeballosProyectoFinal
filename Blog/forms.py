from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from Blog.models import Avatar, POST

class UsuarioRegistro(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label = "contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "repita contraseña", widget=forms.PasswordInput)
    
    class Meta:
        
        model = User
        fields =["username", "email", "first_name", "last_name", "password1","password2"]

class AvatarFormulario(forms.ModelForm):
    
    class Meta:
        
        model = Avatar
        fields = ["imagen"]
        
class FormularioEditar(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "repita contraseña", widget=forms.PasswordInput)
    
    class Meta:
        
        model = User
        fields =["email", "first_name", "last_name", "password1","password2"]
        
class FormularioPOST(forms.ModelForm):
    
    class Meta:
        
        model = POST
        fields =["titulo","subtitulo","nombre", "apellido","contenido"]
        