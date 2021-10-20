from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from products.models import Product, ProductsCategory
import os
import json


# MODULE_DIR = os.path.dirname(__file__)

# Create your views here.


def index(request):
    context = {'title': 'geekshop'}
    return render(request, 'index.html', context)


def products(request, id=None, page=1):
    products = Product.objects.filter(category_id=id) if id is not None else Product.objects.all()
    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {'title': 'catalogue', 'category': ProductsCategory.objects.all(), 'products': products_paginator}
    # context.update({'products': Product.objects.filter(category_id=id) if id is not None else Product.objects.all()})
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
