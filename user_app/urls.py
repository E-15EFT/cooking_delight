from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("signup/", views.user_signup, name="signup"),
    path("logout/", views.user_logout, name="logout"),
    path('public-profile/<str:username>/', views.public_profile, name="public-profile"),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]
