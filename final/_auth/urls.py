from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path, include




urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair')
]