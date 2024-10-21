from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('gamerules', views.gamerules, name="gamerules"),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('community', views.community, name='community'),
    path('create_character', views.create_character, name='create_character'),
    path('forum', views.forum, name='forum'),
]