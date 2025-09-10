# accounts/urls.py

from django.urls import path
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
    UserProfileView,
    FollowToggleView, # We will reuse this view, but modify the logic
    UserProfileDetailView,
    FollowView, # A new view or logic is needed for this pattern
    UnfollowView # A new view or logic is needed for this pattern
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/<str:username>/', UserProfileDetailView.as_view(), name='profile-detail'),
    # New patterns to meet the requirements
    path('follow/<int:user_id>/', FollowToggleView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', FollowToggleView.as_view(), name='unfollow-user'),
]