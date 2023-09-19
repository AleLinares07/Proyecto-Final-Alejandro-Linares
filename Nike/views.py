from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import *
from .forms import *

# Create your views here.
def inicio(req):
    try:

        avatar = Avatar.objects.get(user=req.user.id)
        return render (req, "inicio.html", {"url": avatar.imagen.url})
    except:
        return render (req, "inicio.html")

def zapatillas(req):
   
   zapatillas = Zapatillas.objects.all()
   return render (req, "zapatillas.html", {"zapatillas": zapatillas})

def buzos(req):
   
   buzos = Buzos.objects.all()
   return render (req, "buzos.html", {"buzos": buzos})

def pantalones(req):
   
   pantalones = Pantalones.objects.all()
   return render (req, "pantalones.html", {"pantalones": pantalones})

def añadir_stock_zapatillas(req):

    print('method', req.method)
    print('post', req.POST)

    if req.method == 'POST':

        miFormulario = AñadirStock(req.POST)
        if miFormulario.is_valid():
            
            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data
            producto = Zapatillas(modelo=data["modelo"], color=data["color"], talle=data["talle"])
            producto.save()
            return render(req, "inicio.html", {"mensaje": "Producto ingresado con éxito!"})
        else:
            return render(req, "inicio.html", {"mensaje": "Producto inválido"})
    else:
        miFormulario = AñadirStock()
        return render(req, "añadir_stock_zapatillas.html", {"miFormulario": miFormulario})

def añadir_stock_buzos(req):

    print('method', req.method)
    print('post', req.POST)

    if req.method == 'POST':

        miFormulario = AñadirStock(req.POST)
        if miFormulario.is_valid():
            
            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data
            producto = Buzos(modelo=data["modelo"], color=data["color"], talle=data["talle"])
            producto.save()
            return render(req, "inicio.html", {"mensaje": "Producto ingresado con éxito!"})
        else:
            return render(req, "inicio.html", {"mensaje": "Producto inválido"})
    else:
        miFormulario = AñadirStock()
        return render(req, "añadir_stock_buzos.html", {"miFormulario": miFormulario})

def añadir_stock_pantalones(req):

    print('method', req.method)
    print('post', req.POST)

    if req.method == 'POST':

        miFormulario = AñadirStock(req.POST)
        if miFormulario.is_valid():
            
            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data
            producto = Pantalones(modelo=data["modelo"], color=data["color"], talle=data["talle"])
            producto.save()
            return render(req, "inicio.html", {"mensaje": "Producto ingresado con éxito!"})
        else:
            return render(req, "inicio.html", {"mensaje": "Producto inválido"})
    else:
        miFormulario = AñadirStock()
        return render(req, "añadir_stock_pantalones.html", {"miFormulario": miFormulario})

def busqueda_modelo_zapatillas(req):

    return render(req, "busqueda_modelo.html")

def buscar_zapatillas(req):

    if req.GET["talle"]:
        talle = req.GET["talle"]
        zapatillas = Zapatillas.objects.filter(talle=talle)
        if zapatillas:
            return render(req, "resultado_busqueda_zapatillas.html", {"zapatillas": zapatillas})
    else:
        return HttpResponse (f'No se encontaron resultados')
    
def eliminarZapatillas(req, id):
    if req.method == 'POST':

        zapatillas = Zapatillas.objects.get(id=id)
        zapatillas.delete()

        zapatillas = Zapatillas.objects.all()

        return render(req, "zapatillas.html", {"zapatillas": zapatillas})
    
class ZapatillasList(ListView):
    model = Zapatillas
    template_name = "zapatillas_list.html"
    context_object_name = "zapatillas"

class ZapatillasDetail(DetailView):
    model = Zapatillas
    template_name = "zapatillas_detail.html"
    context_object_name = "zapatilla"

class ZapatillasCreate(LoginRequiredMixin, CreateView):
    model = Zapatillas
    template_name = "zapatillas_create.html"
    fields = ['modelo', 'color', 'talle']
    success_url = '/Nike/'

class ZapatillasUpdate(LoginRequiredMixin, UpdateView):
    model = Zapatillas
    template_name = "zapatillas_update.html"
    fields = ('__all__')
    success_url = '/Nike/'
    context_object_name = "zapatilla"

class ZapatillasDelete(LoginRequiredMixin, DeleteView):
    model = Zapatillas
    template_name = "zapatillas_delete.html"
    success_url = '/Nike/'

def loginView(req):

    if req.method == 'POST':

        miFormulario = AuthenticationForm(req, data=req.POST)
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f'Bienvenido {usuario}'})
            else:
                return render(req, "inicio.html", {"mensaje": "Datos incorrectos"})
        else:
            return render(req,"inicio.html", {"mensaje": "Formulario inválido"})
    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFormulario": miFormulario})
    
def register(req):

    if req.method == 'POST':

        miFormulario = UserCreationForm(req.POST)
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data

            usuario = data['username']

            miFormulario.save()

            return render(req, "inicio.html", {"mensaje": f'Usuario {usuario} creado con exito!'})

        else:
            return render(req,"inicio.html", {"mensaje": "Formulario inválido"})
    else:
        miFormulario = UserCreationForm()
        return render(req, "registro.html", {"miFormulario": miFormulario})
    
def editar_perfil(req):

    usuario = req.user

    if req.method == 'POST':
        miFormulario = UserEditForm(req.POST, instance=req.user)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data['last_name']
            usuario.email = data['email']
            usuario.set_password(data["password1"])
            usuario.save()
            return render(req, "inicio.html", {"mensaje": "Perfil actualizado con éxito."})
        else:
            return render(req, "editarPerfil.html", {"miFormulario": miFormulario})  
    else:
        miFormulario = UserEditForm(instance=req.user)

        return render(req, "editarPerfil.html", {"miFormulario": miFormulario})
    
class BuzosList(ListView):
    model = Buzos
    template_name = "buzos_list.html"
    context_object_name = "buzos"

class BuzosDetail(DetailView):
    model = Buzos
    template_name = "buzos_detail.html"
    context_object_name = "buzo"

class BuzosCreate(LoginRequiredMixin, CreateView):
    model = Buzos
    template_name = "buzos_create.html"
    fields = ['modelo', 'color', 'talle']
    success_url = '/Nike/'

class BuzosUpdate(LoginRequiredMixin, UpdateView):
    model = Buzos
    template_name = "buzos_update.html"
    fields = ('__all__')
    success_url = '/Nike/'
    context_object_name = "buzo"

class BuzosDelete(LoginRequiredMixin, DeleteView):
    model = Buzos
    template_name = "buzos_delete.html"
    success_url = '/Nike/'

class PantalonesList(ListView):
    model = Pantalones
    template_name = "pantalones_list.html"
    context_object_name = "pantalones"

class PantalonesDetail(DetailView):
    model = Pantalones
    template_name = "pantalones_detail.html"
    context_object_name = "pantalon"

class PantalonesCreate(LoginRequiredMixin, CreateView):
    model = Pantalones
    template_name = "pantalones_create.html"
    fields = ['modelo', 'color', 'talle']
    success_url = '/Nike/'

class PantalonesUpdate(LoginRequiredMixin, UpdateView):
    model = Pantalones
    template_name = "pantalones_update.html"
    fields = ('__all__')
    success_url = '/Nike/'
    context_object_name = "buzo"

class PantalonesDelete(LoginRequiredMixin, DeleteView):
    model = Pantalones
    template_name = "pantalones_delete.html"
    success_url = '/Nike/'

def agregarAvatar(req):

    if req.method == 'POST':

        miFormulario = AvatarFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data

            avatar = Avatar(user=req.user, imagen=data["imagen"])

            avatar.save()

            return render(req, "inicio.html", {"mensaje": f'Avatar actualizado con exito!'})

        else:
            return render(req,"inicio.html", {"mensaje": "Formulario inválido"})
    else:
        miFormulario = AvatarFormulario()
        return render(req, "agregar_avatar.html", {"miFormulario": miFormulario})
    
def about(req):
    return render(req, "about.html")

def contact(req):
    return render(req, "contact.html")

def termsofuse(req):
    return render(req, "termsofuse.html")

def privacypolicy(req):
    return render(req, "privacypolicy.html")