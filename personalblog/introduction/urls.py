from django.urls import path, include 
from . import views


urlpatterns = [
    path("", views.introduction, name="introduction"),
    path('aboutme/', views.aboutmyself, name='aboutme')
   
]

