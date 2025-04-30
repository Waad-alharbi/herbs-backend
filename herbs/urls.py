from django.urls import path
from .views import  HerbListCreateView


urlpatterns = [
   
    path('herbs/', HerbListCreateView.as_view(), name='herb-list-create'),

    
]