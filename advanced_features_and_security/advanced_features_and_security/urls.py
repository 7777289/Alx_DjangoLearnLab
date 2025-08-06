from django.contrib import admin
from django.urls import path, include  # include added

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # <- include this
]
