from django.urls import path
from .views import TourListAPIView, CategoryListAPIView

urlpatterns = [
    path('tours/', TourListAPIView.as_view(), name='tour-list'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
]