# Django Relationship Queries

This document provides sample Django ORM queries for models involving:
- ForeignKey
- ManyToManyField
- OneToOneField

## Models Summary

- **Author** – linked to Book via ForeignKey
- **Book** – linked to Author and Library
- **Library** – linked to Book via ManyToManyField
- **Librarian** – linked to Library via OneToOneField

---

## 📚 Query: Books by a specific author

```python
author = Author.objects.get(name="John Doe")
books = author.book_set.all()
