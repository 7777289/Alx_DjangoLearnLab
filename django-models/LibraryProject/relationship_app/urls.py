from django.urls import path
from .views import list_books, LibraryDetailView
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('books/')),  # Redirect root to /books/
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
