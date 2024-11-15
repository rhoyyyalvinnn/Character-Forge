from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('gamerules', views.gamerules, name="gamerules"),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('community', views.community, name='community'),
    path('forum', views.forum, name='forum'),
]