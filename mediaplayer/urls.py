from django.urls import path
from . import views 
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("play-movie/<slug:slug>/", views.play_movie, name="play-movie"),
    path("add-movie/", views.add_movie, name="add-movie"),
    path('add-like/<slug:slug>/', views.like, name='add-like'),
]
   
   
      








