from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("login/auth", views.loginauth, name="loginauth"),
    path("logout", views.logoutreq, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
]