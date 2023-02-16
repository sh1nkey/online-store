from django.shortcuts import render
from products.models import Product, ProductCategory

# Create your views here.

# Функции, т.е. контроллеры, т.е. вьюхи

def index(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Каталог',
        'products' : Product.objects.all(),
        'categories ': ProductCategory.objects.all()

    }
    return render(request, 'products/products.html', context)