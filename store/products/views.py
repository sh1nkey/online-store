from django.shortcuts import render

# Create your views here.

# Функции, т.е. контроллеры, т.е. вьюхи

def index(request):
    return render(request, 'products/index.html',)

def products(request):
    return render(request, 'products/products.html',)