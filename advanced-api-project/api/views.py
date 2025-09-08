# api/views.py
from django.db.models import Prefetch
from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter
from .pagination import DefaultPagination

class BookListView(generics.ListAPIView):
    """
    GET /api/books/?search=python&ordering=-published_date&min_date=2020-01-01&mine=1
    """
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BookFilter
    search_fields = ["title", "author"]
    ordering_fields = ["published_date", "title", "id"]
    ordering = ["-published_date"]

    def get_queryset(self):
        # Optimize for owner relation; avoid N+1
        qs = Book.objects.select_related("owner")
        # Optional: limit columns carefully if you know exactly what serializer needs
        # qs = qs.only("id", "title", "author", "published_date", "owner__username", "slug", "created_at", "updated_at")

        # Custom query param: ?mine=1 returns only the authenticated user's books
        mine = self.request.query_params.get("mine")
        if mine and self.request.user.is_authenticated:
            qs = qs.filter(owner=self.request.user)
        return qs
