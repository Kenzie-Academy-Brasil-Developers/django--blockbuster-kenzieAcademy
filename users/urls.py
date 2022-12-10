from django.urls import path
from rest_framework_simplejwt import views as jwt

from . import views

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/<int:user_id>/", views.UserDetailView.as_view()),
    path("users/login/", jwt.TokenObtainPairView.as_view()),
    path("users/refresh/", jwt.TokenRefreshView.as_view()),
]
