from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('/create_user',views.create_user),
    path('/lancer_reg',views.lancer_reg),
    path('/lancer_info',views.info),
    path('/login',views.login),
    path('/logout',views.logout),
    
]
