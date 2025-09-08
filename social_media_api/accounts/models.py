# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom User model extending AbstractUser.
    Includes additional fields for user profile information
    and a many-to-many relationship for following other users.
    """
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    # Many-to-many relationship for following, using a through model
    following = models.ManyToManyField(
        "self",
        through="UserFollow",
        related_name="followers",
        symmetrical=False,
    )

    def __str__(self):
        return self.username

class UserFollow(models.Model):
    """
    Intermediate model for the many-to-many relationship between users.
    This model allows us to store extra information like the timestamp
    when a user started following another.
    """
    user = models.ForeignKey(User, related_name="following_relations", on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name="follower_relations", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensures that a user can only follow another user once
        unique_together = ('user', 'follower')

    def __str__(self):
        return f"{self.follower.username} follows {self.user.username}"