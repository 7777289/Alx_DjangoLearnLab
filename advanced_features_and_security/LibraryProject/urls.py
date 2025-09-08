from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('relationship_app.urls')),
    path('', include('bookshelf.urls')),  # this line is critical
    path('', RedirectView.as_view(url='/books/', permanent=False)),  # 🔁 redirect root to /books/
]
