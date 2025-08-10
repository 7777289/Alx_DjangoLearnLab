from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # enable filter, search, ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # exact-field filters
    filterset_fields = ['title', 'author', 'publication_year']

    # text search (partial, case-insensitive)
    search_fields = ['title', 'author']

    # fields front-end can order by
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
