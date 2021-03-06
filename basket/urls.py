from django.contrib import admin
from django.urls import path

from basket.views import basket_add, basket_remove, basket_edit

app_name = 'basket'

urlpatterns = [
    path('basket_add/<int:id>', basket_add, name='basket_add'),
    path('basket_remove/<int:id>', basket_remove, name='basket_remove'),
    path('basket_edit/<int:id>/<int:quantity>/', basket_edit, name='basket_edit'),
]
