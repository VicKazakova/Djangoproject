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

from .views import index, admin_users, admin_users_delete, admin_users_update, admin_users_create, \
    admin_products, admin_category, admin_category_create, admin_products_create, \
    admin_products_update, admin_products_delete, admin_category_update, admin_category_delete

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('admin_users/', admin_users, name='admin_users'),
    path('admin_users_delete/<int:id>/', admin_users_delete, name='admin_users_delete'),
    path('admin_users_update/<int:id>/', admin_users_update, name='admin_users_update'),
    path('admin_users_create/', admin_users_create, name='admin_users_create'),
    path('admin_products/', admin_products, name='admin_products'),
    path('admin_category/', admin_category, name='admin_category'),
    path('admin_category_create/', admin_category_create, name='admin_category_create'),
    path('admin_products_create/', admin_products_create, name='admin_products_create'),
    path('admin_products_update/<int:id>/', admin_products_update, name='admin_products_update'),
    path('admin_products_delete/<int:id>/', admin_products_delete, name='admin_products_delete'),
    path('admin_category_update/<int:id>/', admin_category_update, name='admin_category_update'),
    path('admin_category_delete/<int:id>/', admin_category_delete, name='admin_category_delete'),
]
