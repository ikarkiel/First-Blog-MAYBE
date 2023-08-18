from django.urls import path, include 
from . import views


urlpatterns = [
    path("", views.introduction, name="introduction"),
    path("<str:name>", views.greet, name="greet"),
    path("furkan", views.furkan, name="furkan"),
    path("xd", views.xd, name="xd"),
   
]

