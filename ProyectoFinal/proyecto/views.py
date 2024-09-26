from django.shortcuts import render, redirect
from .models import Cliente, Producto, Pedido
from .forms import ClienteForm, PedidoForm, ProductoForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

@login_required
def index(request):
    return render(request, "proyecto/index.html")

@login_required
def cliente_list(request):
    query = Cliente.objects.all()
    context = {"object_list": query}
    return render(request, "proyecto/cliente_list.html", context)

@login_required
def producto_list(request):
    query = Producto.objects.all()
    context = {"object_list": query}
    return render(request, "proyecto/producto_list.html", context)

@login_required
def pedido_list(request):
    query = Pedido.objects.all()
    context = {"object_list": query}
    return render(request, "proyecto/pedido_list.html", context)

@login_required
def cliente_create(request):
    if request.method == "GET":
        form = ClienteForm()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente_list")
    return render(request, "proyecto/cliente_create.html", {"form": form})

@login_required
def producto_create(request):
    if request.method == "GET":
        form = ProductoForm()
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto_list")
    return render(request, "proyecto/producto_create.html", {"form": form})

@login_required
def pedido_create(request):
    if request.method == "GET":
        form = PedidoForm()
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pedido_list")
    return render(request, "proyecto/pedido_create.html", {"form": form})


# Actualizar y Eliminar Cliente
@login_required
def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("cliente_list")
    else:
        form = ClienteForm(instance=cliente)
    return render(request, "proyecto/cliente_update.html", {"form": form})


@login_required
def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect("cliente_list")
    return render(request, "proyecto/cliente_delete.html", {"cliente": cliente})


# Actualizar y Eliminar Producto
@login_required
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("producto_list")
    else:
        form = ProductoForm(instance=producto)
    return render(request, "proyecto/producto_update.html", {"form": form})


@login_required
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect("producto_list")
    return render(request, "proyecto/producto_delete.html", {"producto": producto})


# Actualizar y Eliminar Producto
@login_required
def pedido_update(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect("pedido_list")
    else:
        form = PedidoForm(instance=pedido)
    return render(request, "proyecto/pedido_update.html", {"form": form})

@login_required
def pedido_delete(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        pedido.delete()
        return redirect("pedido_list")
    return render(request, "proyecto/pedido_delete.html", {"pedido": pedido})


# About
@login_required
def about(request):
    return render(request, "proyecto/about.html")

# Registro de Usuario
@login_required
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'proyecto/signup.html', {'form': form})

