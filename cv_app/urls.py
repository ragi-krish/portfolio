from django.contrib import admin
from django.urls import path
from cv_app import views
urlpatterns = [
    path('',views.home,name='home'),
    #path('downloadfile',views.downloadfile, name='downloadfile'),
]
