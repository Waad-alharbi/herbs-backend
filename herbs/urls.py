from django.urls import path
from .views import  (HerbListCreateView, 
HerbDetailView, 
CategoryListAPIView, 
HealthTrackerListCreateView, HealthlogDetailView, 
SignUpView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
   
    path('herbs/', HerbListCreateView.as_view(), name='herb-list-create'),
    path('herbs/<int:pk>/', HerbDetailView.as_view(), name='herb_detail'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('healthtracker/', HealthTrackerListCreateView.as_view(), name='health-tracker-list-create'),
    path('healthtracker/<int:pk>/', HealthlogDetailView.as_view(), name='health_log_detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name='signup')

    
]