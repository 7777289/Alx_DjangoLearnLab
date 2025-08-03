from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
