from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include("cart.urls")),
    path('orders/', include("orders.urls")),
    path('payment/', include('payment.urls')),
    path('coupons/', include('coupons.urls')),
    path('', include("shop.urls")),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)