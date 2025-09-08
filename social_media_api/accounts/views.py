# accounts/views.py

from rest_framework import generics, status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from django.shortcuts import get_object_or_404
from django.db.models import Count

from .models import User
from .serializers import UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    """
    API view for user registration.
    Allows new users to create an account.
    """
    queryset = User.objects.all()
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
    queryset = User.objects.all().annotate(
        followers_count=Count('followers'),
        following_count=Count('following')
    )
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    lookup_field = 'username'

class FollowToggleView(APIView):
    """
    API view to follow or unfollow a user.
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, pk, format=None):
        target_user = get_object_or_404(User, pk=pk)
        current_user = request.user

        if current_user == target_user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user is already following the target user
        is_following = current_user.following.filter(pk=target_user.pk).exists()

        if is_following:
            current_user.following.remove(target_user)
            return Response({"detail": f"You have unfollowed {target_user.username}."}, status=status.HTTP_200_OK)
        else:
            current_user.following.add(target_user)
            return Response({"detail": f"You are now following {target_user.username}."}, status=status.HTTP_201_CREATED)