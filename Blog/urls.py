from django.contrib import admin
from django.urls import path
from django.urls import include
from Blog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/", inicio, name="INICIO"),
    path("contact/", contact, name="CONTACT"),
    path("about/", about, name="ABOUT"),
    path("post/", post, name="POST"),
    path("resultados/", resultados, name="RESULTADOS"),
    path("inexistente/", Vacio, name="VACIO"),
    
    
    #FORMULAROS DE LOG
    path("registro/", registro, name="REGISTRO"),
    path("ingresar/", ingresar, name="INGRESAR"),
    path("logout", LogoutView.as_view(template_name="Blog/logout.html"), name="LOGOUT"),
    path("editar/",editar, name="USEREDITAR"),
    
    path("agregarAvatar/", agregarAvatar, name="AGREGARAVATAR"),
    
    #CRUD formularios de POST
    path("formularioPOST/", formularioPOST, name="FORMULARIOPOSTS"),
    
    #CRUD POST LIST
    path ("POST/list", ListaPOST.as_view(), name="LISTAPOST"),
    path ("POST/<int:pk>", DetallePOST.as_view(), name="DETALLEPOST"),
    path ("POST/crear/", CrearPOST.as_view(), name="CREARPOST"),
    path ("POST/editar/<int:pk>", ActualizarPOST.as_view(), name="ACTUALIZARPOST"),
    path ("POST/borrar/<int:pk>", BorrarPOST.as_view(), name="BORRARPOST"),
    
]