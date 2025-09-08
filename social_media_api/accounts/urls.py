# accounts/urls.py

from django.urls import path
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
    UserProfileView,
    FollowToggleView,
    UserProfileDetailView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/<str:username>/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('users/<int:pk>/follow/', FollowToggleView.as_view(), name='follow-toggle'),
]