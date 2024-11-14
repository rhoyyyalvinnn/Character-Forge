from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.profile, name='profile'),
    path('actcommunity/', views.actcommunity, name='actcommunity'),
    path('actforum/', views.actforum, name='actforum'),
    path('actgamerules/', views.actgamerules, name='actgamerules'),
]