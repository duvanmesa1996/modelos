from django.urls import path
from django.urls import listar_clientes, listar_prodoctos

urlpatterns = [
    path('productos/', listar_Profuctos,
    name = 'listar_productos'), 
    path('clientes/', listar_cliente,
    name = 'listar_clientes'), 
]
