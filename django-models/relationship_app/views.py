# relationship_app/views.py
from django.views.generic import DetailView
from django.shortcuts import render
from .models import Book, Library

def book_list(request):
    """
    A function-based view to list all books.
    """
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'list_books.html', context)

class LibraryDetailView(DetailView):
    """
    A class-based view to display details of a specific library.
    """
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
