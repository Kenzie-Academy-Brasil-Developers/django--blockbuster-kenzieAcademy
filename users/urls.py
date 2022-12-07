from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UserViews.as_view()),
    path("users/login/", views.LoginViews.as_view()),
]
