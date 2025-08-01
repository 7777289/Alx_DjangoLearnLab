# Delete Operation

This operation deletes the book and confirms that the database is now empty.

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# <QuerySet []>
