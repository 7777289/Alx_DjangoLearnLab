from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from relationship_app.views import list_books, LibraryDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('', lambda request: redirect('books/')),  # 👈 Redirect root to /books/
]
