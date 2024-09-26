"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from proyecto import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ruta principal
    path("", views.index, name="index"),

    # Rutas para Cliente
    path("cliente/list/", views.cliente_list, name="cliente_list"),
    path("cliente/create/", views.cliente_create, name="cliente_create"),
    path("cliente/<int:pk>/edit/", views.cliente_update, name="cliente_update"),
    path("cliente/<int:pk>/delete/", views.cliente_delete, name="cliente_delete"),

    # Rutas para Producto
    path("producto/list/", views.producto_list, name="producto_list"),
    path("producto/create/", views.producto_create, name="producto_create"),
    path("producto/<int:pk>/edit/", views.producto_update, name="producto_update"),
    path("producto/<int:pk>/delete/", views.producto_delete, name="producto_delete"),

    # Rutas para Pedido
    path("pedido/list/", views.pedido_list, name="pedido_list"),
    path("pedido/create/", views.pedido_create, name="pedido_create"),
    path("pedido/<int:pk>/edit/", views.pedido_update, name="pedido_update"),
    path("pedido/<int:pk>/delete/", views.pedido_delete, name="pedido_delete"),

    # Rutas para About
    path("about/", views.about, name="about"),

    # Rutas para Login y Logout
    path("login/", auth_views.LoginView.as_view(template_name="proyecto/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Rutas para Registro de Usuario
    path('signup/', views.signup, name='signup'),

]