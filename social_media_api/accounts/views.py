# accounts/views.py

from rest_framework import generics, status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from django.shortcuts import get_object_or_404
from django.db.models import Count

from .models import CustomUser, UserFollow
from .serializers import UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    """
    API view for user registration.
    Allows new users to create an account.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(ObtainAuthToken):
    """
    API view for user login.
    Returns a token upon successful authentication.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

class UserLogoutView(APIView):
    """
    API view for user logout.
    Deletes the authentication token.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, Token.DoesNotExist):
            return Response({"detail": "Token not provided or invalid."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    API view to retrieve and update the authenticated user's profile.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        return self.request.user

class UserProfileDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve another user's public profile by username.
    """
    queryset = CustomUser.objects.all().annotate(
        followers_count=Count('followers'),
        following_count=Count('following')
    )
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'username'

class FollowView(APIView):
    """
    API view to follow a user.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        target_user = get_object_or_404(CustomUser, pk=user_id)
        current_user = request.user

        if current_user == target_user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user is already followed
        if UserFollow.objects.filter(user=target_user, follower=current_user).exists():
            return Response({"detail": "You are already following this user."}, status=status.HTTP_409_CONFLICT)
        
        # Create the follow relationship
        UserFollow.objects.create(user=target_user, follower=current_user)
        return Response({"detail": f"You are now following {target_user.username}."}, status=status.HTTP_201_CREATED)

class UnfollowView(APIView):
    """
    API view to unfollow a user.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        target_user = get_object_or_404(CustomUser, pk=user_id)
        current_user = request.user

        if current_user == target_user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Find and delete the follow relationship
        follow_instance = UserFollow.objects.filter(user=target_user, follower=current_user)
        if follow_instance.exists():
            follow_instance.delete()
            return Response({"detail": f"You have unfollowed {target_user.username}."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "You are not following this user."}, status=status.HTTP_404_NOT_FOUND)

# The original FollowToggleView is no longer needed with the new separate views
# but can be kept for reference if needed.
# class FollowToggleView(generics.GenericAPIView):
#     """
#     API view to follow or unfollow a user.
#     """
#     ...