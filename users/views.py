from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, UpdateView

from .forms import UserLoginForm, UserRegisterForm, UserProfileForm, UserProfileEditForm
from basket.models import Basket

# Create your views here.
from .models import User


class LoginListView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('users:profile')

    def get_context_data(self, **kwargs):
        context = super(LoginListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Авторизация'
        return context


# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user and user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#
#     else:
#         form = UserLoginForm()
#     context = {
#         'title': 'Geekshop -- Авторизация',
#         'form': form
#     }
#     return render(request, 'users/login.html', context)


class RegisterListView(FormView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super(RegisterListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Регистрация'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save()
            if self.send_verify_link(user):
                messages.success(request, 'Вы успешно зарегистрировались!')
                return redirect(self.success_url)
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})

    @staticmethod
    def send_verify_link(user):
        verify_link = reverse('users:verify', args=[user.email, user.activation_key])
        subject = f'Для активации учетной записи {user.username} пройдите по ссылке'
        message = f'Для подтверждения учетной записи {user.username} на портале \n {settings.DOMAIN_NAME}{verify_link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

    @staticmethod
    def verify(request, email, activation_key):
        try:
            user = User.objects.get(email=email)
            if user and user.activation_key == activation_key and not user.if_activation_key_expired():
                user.activation_key = ''
                user.activation_key_expires = None
                user.is_active = True
                user.save()
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'users/verification.html')
        except Exception as e:
            # print(e)
            return HttpResponseRedirect(reverse('index'))


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             if send_verify_link(user):
#                 messages.success(request, "Registration successful!")
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegisterForm()
#     context = {
#         'title': 'Geekshop -- Регистрация',
#         'form': form
#     }
#     return render(request, 'users/register.html', context)


class ProfileFormView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    form_class_second = UserProfileEditForm
    success_url = reverse_lazy('users:profile')

    def get_context_data(self, **kwargs):
        context = super(ProfileFormView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Профиль'
        context['profile_form'] = self.form_class_second(instance=self.request.user.userprofile)

        return context

    def get_object(self, *args, **kwargs):
        return get_object_or_404(User, pk=self.request.user.pk)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        user = self.get_object()
        edit_form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
        profile_form = UserProfileEditForm(data=request.POST, files=request.FILES, instance=user.userprofile)

        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, {
            'form': edit_form,
            'profile_form': profile_form,
        })


# @login_required
# def profile(request):
#     final_quantity = 0
#     final_sum = 0
#     baskets = Basket.objects.filter(user=request.user)
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
#         profile_form = UserProfileEditForm(data=request.POST, instance=request.user.userprofile)
#         if form.is_valid() and profile_form.is_valid():
#             form.save()
#             messages.success(request, "Your data changed successfully!")
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#         form = UserProfileForm(instance=request.user)
#         profile_form = UserProfileEditForm(instance=request.user.userprofile)
#         if baskets:
#             for basket in baskets:
#                 final_quantity += basket.quantity
#                 final_sum += basket.sum()
#     context = {
#         'title': 'Geekshop -- Профиль',
#         'form': form,
#         'baskets': baskets,
#         'final_quantity': final_quantity,
#         'final_sum': final_sum,
#         'profile_form': profile_form
#     }
#     return render(request, 'users/profile.html', context)

class Logout(LogoutView):
    template_name = "index.html"

# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))


# def send_verify_link(user):
#     verify_link = reverse('users:verify', args=[user.email, user.activation_key])
#     subject = f'For activation {user.username} follow the link:'
#     message = f'For your login confirmation {user.username} follow the link:' \
#               f'{settings.DOMAIN_NAME}{verify_link}'
#     return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
