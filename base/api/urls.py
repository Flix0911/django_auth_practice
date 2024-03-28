from django.urls import path
from . import views
from .views import MyTokenObtainPairView

# as per docs
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    
    # don't need to prefix it with api/ ~ we already have that
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]