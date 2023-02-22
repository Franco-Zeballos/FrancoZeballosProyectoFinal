from django.shortcuts import render
from django.http import HttpResponse
from Blog.forms import *
from Blog.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
import os

# Create your views here.
def inicio(request):
    
    return render(request, "Blog/inicio.html")
def post(request):
    
    return render(request, "Blog/post.html")
def contact(request):
    
    return render(request, "Blog/contact.html")
def about(request):
    
    return render(request, "Blog/about.html")

#LOG FORMS
def registro(request):
    
    if request.method == "POST":
        
        form = UsuarioRegistro(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "Blog/inicio.html", {"mensaje": "Usuario Creado"})
        
    else:
        
        form = UsuarioRegistro()
        
    return render(request, "Blog/registro.html", {"formulario":form})
def ingresar(request):
    
    if request.method == "POST":
    
        form = AuthenticationForm(request, data = request.POST)
            
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username = usuario, password = contra)
            
            if user:
                
                login(request, user)
                
                return render(request, "Blog/inicio.html", {"mensaje":f"Bienvenido, {user}"})
        
        else:
            return render(request, "Blog/inicio.html", {"mensaje":"Datos incorrectos"}) 
    else:
        form = AuthenticationForm()
    return render(request, "Blog/ingresar.html", {"formulario":form})
@login_required
def editar(request):
    
    usuario = request.user
    
    if request.method == "POST":
        
        form = FormularioEditar(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"] 
            usuario.last_name = info["last_name"]
            usuario.save()
            return render(request, "Blog/inicio.html", {"mensaje":f"Se han actualizado los datos"})
    else:
        form = FormularioEditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
        })
    return render(request, "Blog/editarusuario.html", {"formulario":form, "usuario":usuario})

@staff_member_required
def agregarAvatar(request):
    if request.method =="POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            usuarioActual = User.objects.get(username=request.user)

            
            avataresAnteriores = Avatar.objects.filter(usuario=usuarioActual)
            for avatarAnterior in avataresAnteriores:
                avatarAnterior.delete()

            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])
            avatar.save()
            
            print(f"Avatar object created for user {usuarioActual.username} with image {avatar.imagen.name}")

            return render(request, "Blog/inicio.html")
        else:
            print(form.errors)
    else:
        form = AvatarFormulario()

    return render(request, "Blog/agregarAvatar.html", {"formulario":form})

def formularioPOST(request):
    
    if request.method == "POST":
        
        formuP =  FormularioPOST(request.POST)
        
        if formuP.is_valid():
            
            info = formuP.cleaned_data
            
            post = POST(nombre=info["nombre"], 
                        apellido=info["apellido"],
                        contenido=info["contenido"],
                        )
            post.save()
            
            return render(request, "Blog/inicio.html")
    else:
        
        formuP = FormularioPOST()
    
    return render(request, "Blog/formularioPOST.html", {"formP":formuP})

def resultados(request):
    
    if request.GET["nombre"]:
        
        nombre=request.GET["nombre"]
        
        posts = POST.objects.filter(nombre__icontains=nombre)
        
        return render(request, "Blog/resultados.html",{"posts":posts, "nombre":nombre})
    
    else:
        
        respuesta = "No enviaste datos."
    
    return render(request, "Blog/inicio.html", {"mensaje":respuesta})

class ListaPOST(ListView):
    
    model = POST

class DetallePOST(DetailView):
    
    model = POST

class CrearPOST(LoginRequiredMixin, CreateView):
    
    model = POST
    success_url ="/Blog/POST/list"
    fields =["titulo","subtitulo","nombre", "apellido","contenido"]
    
class ActualizarPOST(LoginRequiredMixin, UpdateView):
    model = POST
    success_url ="/Blog/POST/list"
    fields =["titulo","subtitulo","nombre", "apellido","contenido"]
  
class BorrarPOST(LoginRequiredMixin, DeleteView):
    
    model = POST
    success_url ="/Blog/POST/list"
    
def Vacio(request):
    return render(request, "Blog/vacio.html")
