# api_project/urls.py

from django.contrib import admin
from django.urls import path, include  # include is important

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # This line includes your app routes
]
