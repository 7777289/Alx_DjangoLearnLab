from rest_framework import generics, filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]  # Include OrderingFilter
    search_fields = ['title', 'author']  # Already set for Step 2
    ordering_fields = ['title', 'publication_year']  # Allow ordering by these fields
    ordering = ['title']  # Default ordering (optional)


class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Retrieve details of a single book by ID.
    Public read access allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read for all, write restricted


class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Auth required

    def perform_create(self, serializer):
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update an existing book by ID.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Auth required

    def perform_update(self, serializer):
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Remove a book by ID.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Auth required
