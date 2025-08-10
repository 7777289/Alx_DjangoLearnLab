from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# List & create authors, with nested books
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# List & create books
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
