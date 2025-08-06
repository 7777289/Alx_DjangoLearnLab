from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return HttpResponse("This is the registration page.")

def profile(request):
    return HttpResponse("This is the user profile page.")
