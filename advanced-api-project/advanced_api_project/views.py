
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Add filter, search, and ordering backends
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Filtering options
    filterset_fields = ['title', 'author', 'publication_year']

    # Search options
    search_fields = ['title', 'author']

    # Ordering options
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering
