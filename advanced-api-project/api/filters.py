# api/filters.py
import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    min_date = django_filters.DateFilter(field_name="published_date", lookup_expr="gte")
    max_date = django_filters.DateFilter(field_name="published_date", lookup_expr="lte")
    author = django_filters.CharFilter(field_name="author", lookup_expr="icontains")
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Book
        fields = ["author", "title", "min_date", "max_date"]
