from django import forms

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from products.models import ProductsCategory, Product
from basket.models import Basket


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control py-4',
                                                            'placeholder': 'Введите адрес эл. почты'}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                             'readonly': False}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control py-4',
                                                            'readonly': False}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')


class UserAdminProductCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                         'readonly': False}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                                'readonly': False}))
    price = forms.DecimalField(widget=forms.NumberInput())
    quantity = forms.IntegerField(widget=forms.NumberInput())
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    category = forms.IntegerField(widget=forms.NumberInput())

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity', 'image', 'category')


class UserAdminProductCategoryCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                         'readonly': False}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                                'readonly': False}))

    class Meta:
        model = Product
        fields = ('name', 'description')


class UserAdminProductUpdateForm(UserProfileForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                         'readonly': False}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                                'readonly': False}))
    price = forms.CharField(widget=forms.NumberInput())
    quantity = forms.IntegerField(widget=forms.NumberInput())
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    category = forms.IntegerField(widget=forms.NumberInput())

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity', 'image', 'category')


class UserAdminCategoryUpdateForm(UserProfileForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                         'readonly': False}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                                'readonly': False}))

    class Meta:
        model = Product
        fields = ('name', 'description')


class UserAdminBasketCreateForm(forms.ModelForm):
    quantity = forms.IntegerField(widget=forms.NumberInput())

    class Meta:
        model = Basket
        fields = ('user', 'product', 'quantity')


class UserAdminBasketUpdateForm(forms.ModelForm):
    quantity = forms.IntegerField(widget=forms.NumberInput())

    class Meta:
        model = Basket
        fields = ('user', 'product', 'quantity')
