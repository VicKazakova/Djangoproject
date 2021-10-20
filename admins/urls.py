"""Djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from .views import index,\
    UserListView, ProductsListView, CategoryListView, UserCreateView, ProductsCreateView, CategoryCreateView, \
    UserUpdateView, ProductUpdateView, CategoryUpdateView, UserDeleteView, ProductsDeleteView, CategoryDeleteView, \
    BasketListView, BasketCreateView, BasketUpdateView, BasketDeleteView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('admin_users/', UserListView.as_view(), name='admin_users'),
    path('admin_users_delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),
    path('admin_users_update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('admin_users_create/', UserCreateView.as_view(), name='admin_users_create'),
    path('admin_products/', ProductsListView.as_view(), name='admin_products'),
    path('admin_category/', CategoryListView.as_view(), name='admin_category'),
    path('admin_category_create/', CategoryCreateView.as_view(), name='admin_category_create'),
    path('admin_products_create/', ProductsCreateView.as_view(), name='admin_products_create'),
    path('admin_products_update/<int:pk>/', ProductUpdateView.as_view(), name='admin_products_update'),
    path('admin_products_delete/<int:pk>/', ProductsDeleteView.as_view(), name='admin_products_delete'),
    path('admin_category_update/<int:pk>/', CategoryUpdateView.as_view(), name='admin_category_update'),
    path('admin_category_delete/<int:pk>/', CategoryDeleteView.as_view(), name='admin_category_delete'),
    path('admin_basket_read/', BasketListView.as_view(), name='admin_basket_read'),
    path('admin_basket_create/', BasketCreateView.as_view(), name='admin_basket_create'),
    path('admin_basket_update/<int:pk>/', BasketUpdateView.as_view(), name='admin_basket_update'),
    path('admin_basket_delete/<int:pk>/', BasketDeleteView.as_view(), name='admin_basket_delete'),
]
