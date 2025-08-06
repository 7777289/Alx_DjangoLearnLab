from .forms import ExampleForm

from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Example placeholder logic for creating a book
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Example placeholder logic for editing a book
    return render(request, 'bookshelf/edit_book.html', {'book_id': book_id})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # Example placeholder logic for deleting a book
    return render(request, 'bookshelf/delete_book.html', {'book_id': book_id})
