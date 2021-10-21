from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, \
    UserAdminProductCreateForm, UserAdminProductCategoryCreateForm, \
    UserAdminCategoryUpdateForm, UserAdminProductUpdateForm, UserAdminBasketCreateForm, UserAdminBasketUpdateForm
from users.models import User
from products.models import Product, ProductsCategory
from basket.models import Basket


def index(request):
    return render(request, 'admins/admin.html')


# ------------------------------------------------READ-----------------------------------------------


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop Admin | Users'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class ProductsListView(ListView):
    model = Product
    template_name = 'admins/admin-products-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop Admin | Products'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsListView, self).dispatch(request, *args, **kwargs)


class CategoryListView(ListView):
    model = ProductsCategory
    template_name = 'admins/admin-category-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop Admin | Categories'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryListView, self).dispatch(request, *args, **kwargs)


class BasketListView(ListView):
    model = Basket
    template_name = 'admins/admin-baskets-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BasketListView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop Admin | Baskets'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(BasketListView, self).dispatch(request, *args, **kwargs)


# ------------------------------------------------CREATE-----------------------------------------------


class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop Admin | Users'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


class ProductsCreateView(CreateView):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = UserAdminProductCreateForm
    success_url = reverse_lazy('admins:admin_products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop Admin | Products'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsCreateView, self).dispatch(request, *args, **kwargs)


class CategoryCreateView(CreateView):
    model = ProductsCategory
    template_name = 'admins/admin-category-create.html'
    form_class = UserAdminProductCategoryCreateForm
    success_url = reverse_lazy('admins:admin_category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop Admin | Categories'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryCreateView, self).dispatch(request, *args, **kwargs)


class BasketCreateView(CreateView):
    model = Basket
    template_name = 'admins/admin-baskets-create.html'
    form_class = UserAdminBasketCreateForm
    success_url = reverse_lazy('admins:admin_basket_read')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BasketCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop Admin | Basket'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(BasketCreateView, self).dispatch(request, *args, **kwargs)

# ------------------------------------------------UPDATE-----------------------------------------------


class UserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop Admin | Users'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = UserAdminProductUpdateForm
    success_url = reverse_lazy('admins:admin_products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop Admin | Products'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)


class CategoryUpdateView(UpdateView):
    model = ProductsCategory
    template_name = 'admins/admin-category-update-delete.html'
    form_class = UserAdminCategoryUpdateForm
    success_url = reverse_lazy('admins:admin_category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop Admin | Categories'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryUpdateView, self).dispatch(request, *args, **kwargs)


class BasketUpdateView(UpdateView):
    model = Basket
    template_name = 'admins/admin-baskets-update-delete.html'
    form_class = UserAdminBasketUpdateForm
    success_url = reverse_lazy('admins:admin_basket_read')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BasketUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop Admin | Baskets'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(BasketUpdateView, self).dispatch(request, *args, **kwargs)

# ------------------------------------------------DELETE-----------------------------------------------


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductsDeleteView(DeleteView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admin_products')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoryDeleteView(DeleteView):
    model = ProductsCategory
    template_name = 'admins/admin-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_category')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class BasketDeleteView(DeleteView):
    model = Basket
    template_name = 'admins/admin-baskets-update-delete.html'
    success_url = reverse_lazy('admins:admin_basket_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(BasketDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
