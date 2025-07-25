from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', auth_views.logout_then_login, name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('cabinet', views.CabinetView.as_view(), name="cabinet"),


]