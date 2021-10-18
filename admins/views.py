from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, \
    UserAdminProductCreateForm, UserAdminProductCategoryCreateForm, \
    UserAdminCategoryUpdateForm, UserAdminProductUpdateForm
from users.models import User
from products.models import Product, ProductsCategory


def index(request):
    return render(request, 'admins/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return HttpResponseRedirect(reverse('admins:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'GeekShop - Aдмин |Регистрация',
        'form': form
    }
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, id):
    users_select = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance=users_select, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your data changed successfully!")
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=users_select)
    context = {
        'title': 'Geekshop -- Админ',
        'form': form,
        'users_select': users_select
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active= False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'admins/admin-products-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category(request):
    context = {
        'category': ProductsCategory.objects.all()
    }
    return render(request, 'admins/admin-category-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == 'POST':
        form = UserAdminProductCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
        else:
            print(form.errors)
    else:
        form = UserAdminProductCreateForm()
    context = {
        'title': 'GeekShop - Aдмин | Продукты',
        'form': form
    }
    return render(request, 'admins/admin-products-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_create(request):
    if request.method == 'POST':
        form = UserAdminProductCategoryCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category'))
        else:
            print(form.errors)
    else:
        form = UserAdminProductCategoryCreateForm()
    context = {
        'title': 'GeekShop - Aдмин | Категории',
        'form': form
    }
    return render(request, 'admins/admin-category-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_update(request, id):
    products_select = Product.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProductUpdateForm(data=request.POST, instance=products_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = UserAdminProductUpdateForm(instance=products_select)
    context = {
        'title': 'Geekshop -- Админ',
        'form': form,
        'products_select': products_select
    }
    return render(request, 'admins/admin-products-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_delete(request, id):
    product = Product.objects.get(id=id)
    product.is_active = False
    product.save()
    return HttpResponseRedirect(reverse('admins:admin_products'))


@user_passes_test(lambda u: u.is_superuser)
def admin_category_update(request, id):
    category_select = ProductsCategory.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminCategoryUpdateForm(data=request.POST, instance=category_select)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category'))
    else:
        form = UserAdminCategoryUpdateForm(instance=category_select)
    context = {
        'title': 'Geekshop -- Админ',
        'form': form,
        'category_select': category_select
    }
    return render(request, 'admins/admin-category-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_delete(request, id):
    category = ProductsCategory.objects.get(id=id)
    category.is_active = False
    category.save()
    return HttpResponseRedirect(reverse('admins:admin_category'))
