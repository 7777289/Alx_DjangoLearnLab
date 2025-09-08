# api/serializers.py
from datetime import date
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Book
        fields = ["id", "title", "author", "published_date", "owner", "slug", "created_at", "updated_at"]
        read_only_fields = ["id", "owner", "slug", "created_at", "updated_at"]

    def validate_published_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("published_date cannot be in the future.")
        return value

    def validate(self, attrs):
        """
        Enforce 'title+author' uniqueness (create & update).
        - On update, exclude the current instance.
        """
        title = attrs.get("title", getattr(self.instance, "title", None))
        author = attrs.get("author", getattr(self.instance, "author", None))
        qs = Book.objects.filter(title__iexact=title, author__iexact=author)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("A book with this title and author already exists.")
        return attrs
