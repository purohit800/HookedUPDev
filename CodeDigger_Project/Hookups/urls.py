from django.contrib import admin
from django.urls import path
from Hookups import views

urlpatterns = [
    #hookups
    path('',views.home,name="home"),
    path('join',views.join,name="join"),
 
]
