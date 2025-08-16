from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment


# ---------------- USER FORMS ---------------- #

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


# ---------------- BLOG FORMS ---------------- #

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


# ---------------- COMMENT FORMS ---------------- #

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Write a comment...',
            'rows': 3,
            'cols': 50
        })
    )

    class Meta:
        model = Comment
        fields = ['content']
