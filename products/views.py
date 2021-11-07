from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView

from products.models import Product, ProductsCategory


# import os
# import json


# MODULE_DIR = os.path.dirname(__file__)

def index(request):
    context = {'title': 'geekshop'}
    return render(request, 'index.html', context)


class ProductView(ListView):
    model = Product
    template_name = 'products.html'

    def get_queryset(self, id=None):
        return Product.objects.filter(category_id=id) if id is not None else Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop -- Products'
        return context


class ProductCategoryView(ListView):
    model = ProductsCategory
    template_name = 'products.html'

    def get_queryset(self):
        return ProductsCategory.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoryView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop -- Products'
        return context

# def dispatch(self, request, *args, **kwargs):
#     return super(ProductView, self).dispatch(request, *args, **kwargs)
#
# def get_queryset(self, id=None):
#     return Product.objects.all()

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


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, category_id=None, *args, **kwargs):
        context = super().get_context_data()
        context['categories'] = ProductsCategory.objects.all()
        return context
