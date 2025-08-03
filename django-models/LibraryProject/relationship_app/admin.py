# relationship_app/admin.py

from django.contrib import admin
from .models import Author, Profile, Book, Library, Librarian

admin.site.register(Author)
admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
