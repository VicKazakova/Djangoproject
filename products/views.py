from django.shortcuts import render

from products.models import Product, ProductsCategory
import os
import json

# MODULE_DIR = os.path.dirname(__file__)

# Create your views here.


def index(request):
    context = {'title': 'geekshop'}
    return render(request, 'index.html', context)


def products(request):
    context = {'title': 'catalogue', 'products': Product.objects.all(), 'category': ProductsCategory.objects.all()}
    return render(request, 'products.html', context)


def test(request):
    context = {
        'title': 'geekshop',
        'user': 'Petrov',
        'description': 'Welcome!',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00'},
        ],
        'promotion': True,
        'products_of_promotion': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00'},
        ]
    }
    return render(request, 'test.html', context)
