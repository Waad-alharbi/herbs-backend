from django.urls import path
from .views import  HerbListCreateView, HerbDetailView, CategoryListAPIView


urlpatterns = [
   
    path('herbs/', HerbListCreateView.as_view(), name='herb-list-create'),
    path('herbs/<int:pk>/', HerbDetailView.as_view(), name='herb_detail'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list')

    
]