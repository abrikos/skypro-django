from django.contrib import admin
from django.urls import path

from catalog import views
app_name='catalog'
urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contacts', views.contacts, name="contacts"),
    path('feedback', views.feedback, name="feedback"),
]
