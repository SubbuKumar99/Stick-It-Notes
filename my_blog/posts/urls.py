from django.contrib import admin
from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('newPost/',views.newPost,name='newPost'),
]
