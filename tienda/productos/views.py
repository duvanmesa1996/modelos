from django.shortcuts import render
from.models import cliente
from.models import producto

# Create your views here.

def listar_cliente(request):
    clientes = cliente.objects.all()
    return render(request, 'lista_clientes.html'
    {'clientes':clientes})

def listar_prodoctos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_Profuctos.html'
    {'productos':producto})