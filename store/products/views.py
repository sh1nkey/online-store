from django.shortcuts import render

# Create your views here.

# Функции, т.е. контроллеры, т.е. вьюхи

def index(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Store - Каталог',
    }
    return render(request, 'products/products.html', context)