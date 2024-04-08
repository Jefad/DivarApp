from django.urls import path
from .views import EstateCreateAPIView, EstateDetailAPIView, EstateListView, EstateUpdateView


urlpatterns = [
    path('<int:pk>/', EstateDetailAPIView.as_view(), name='estate-detail'),
    path('create/', EstateCreateAPIView.as_view(), name='estate-create'),
    path('filter/', EstateListView.as_view(), name='estate-filter'),
    path('update/<int:pk>/', EstateUpdateView.as_view(), name='estate-update'),
]
