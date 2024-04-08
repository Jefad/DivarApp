from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.auth_urls')),
    path('api/estate/', include('estate.urls')),
    # path('api/state/', include('estate.location_urls')),
    # path('api/purchase/', include('users.purchase_urls'))
]
