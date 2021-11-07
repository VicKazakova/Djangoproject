from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from products.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('basket/', include('basket.urls', namespace='basket')),
    path('users/', include('users.urls', namespace='users')),
    path('admins/', include('admins.urls', namespace='admins')),
    path('orders/', include('ordersapp.urls', namespace='orders')),
    path('', include('social_django.urls', namespace='social')),
    # path('test/', test, name='test'),
]

# чтобы подтягивать изображения:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
