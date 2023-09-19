from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='Inicio'),
    path('zapatillas/', zapatillas, name='Zapatillas'),
    path('buzos/', buzos, name='Buzos'),
    path('pantalones/', pantalones, name='Pantalones'),
    path('añadir-stock-zapatillas/', añadir_stock_zapatillas, name='AñadirZapatillas'),
    path('añadir-stock-buzos/', añadir_stock_buzos, name='AñadirBuzos'),
    path('añadir-stock-pantalones/', añadir_stock_pantalones, name='AñadirPantalones'),
    path('busqueda-modelo/', busqueda_modelo_zapatillas, name='BusquedaModelo'),
    path('buscar-zapatillas/', buscar_zapatillas, name='BuscarZapatillas'),
    path('zapatillas-list/', ZapatillasList.as_view(), name='ZapatillasList'),
    path('zapatillas-detail/<pk>', ZapatillasDetail.as_view(), name='ZapatillasDetail'),
    path('zapatillas-create/', ZapatillasCreate.as_view(), name='ZapatillasCreate'),
    path('zapatillas-update/<pk>', ZapatillasUpdate.as_view(), name='ZapatillasUpdate'),
    path('zapatillas-delete/<pk>', ZapatillasDelete.as_view(), name='ZapatillasDelete'),
    path('login/', loginView, name='Login'),
    path('registrar/', register, name='Registrar'),
    path('logout/', LogoutView.as_view(template_name ='logout.html'), name='Logout'),
    path('editar-perfil/', editar_perfil, name='EditarPerfil'),
    path('buzos-list/', BuzosList.as_view(), name='BuzosList'),
    path('buzos-detail/<pk>', BuzosDetail.as_view(), name='BuzosDetail'),
    path('buzos-create/', BuzosCreate.as_view(), name='BuzosCreate'),
    path('buzos-update/<pk>', BuzosUpdate.as_view(), name='BuzosUpdate'),
    path('buzos-delete/<pk>', BuzosDelete.as_view(), name='BuzosDelete'),
    path('pantalones-list/', PantalonesList.as_view(), name='PantalonesList'),
    path('pantalones-detail/<pk>', PantalonesDetail.as_view(), name='PantalonesDetail'),
    path('pantalones-create/', PantalonesCreate.as_view(), name='PantalonesCreate'),
    path('pantalones-update/<pk>', PantalonesUpdate.as_view(), name='PantalonesUpdate'),
    path('pantalones-delete/<pk>', PantalonesDelete.as_view(), name='PantalonesDelete'),
    path('agregar-avatar/', agregarAvatar, name='AgregarAvatar'),
    path('about/', about, name='About'),
    path('contact/', contact, name='Contact'),
    path('termsofuse/', termsofuse, name='TermsOfUse'),
    path('privacypolicy/', privacypolicy, name='PrivacyPolicy'),
]