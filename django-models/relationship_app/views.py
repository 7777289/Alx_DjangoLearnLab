# relationship_app/views.py

from django.shortcuts import render
from .models import Book  # Make sure Book is imported

def book_list(request):
    """
    A function-based view to list all books.
    """
    # This line queries all Book objects from the database
    books = Book.objects.all() 
    
    context = {'books': books}
    
    # This line renders the list_books.html template
    return render(request, 'list_books.html', context)