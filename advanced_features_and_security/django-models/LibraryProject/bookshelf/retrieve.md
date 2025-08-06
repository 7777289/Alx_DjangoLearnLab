# Retrieve Operation

This operation retrieves the `Book` instance created earlier and displays its attributes.

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# ('1984', 'George Orwell', 1949)
