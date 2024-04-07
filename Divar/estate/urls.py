from django.urls import path
from .views import EstateCreateAPIView, EstateDetailAPIView, EstateUpdateAPIView


urlpatterns = [
    path('', EstateDetailAPIView.as_view(), name='estate-all-view'),
    path('<int:pk>/', EstateDetailAPIView.as_view(), name='estate-detail'),
    path('create/', EstateCreateAPIView.as_view(), name='estate-create'),
    path('<int:pk>/update/', EstateUpdateAPIView.as_view(), name='estate-update'),
]
