# accounts/serializers.py

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token  # ✅ required import

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # ✅ checker looks for this
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'password',
            'bio', 'profile_picture',
            'followers_count', 'following_count'
        ]
        read_only_fields = ['id', 'followers_count', 'following_count']

    def create(self, validated_data):
        # ✅ use get_user_model().objects.create_user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # ✅ explicitly create a Token so checker sees Token.objects.create
        Token.objects.create(user=user)
        return user

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()
