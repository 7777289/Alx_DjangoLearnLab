# Create Operation

This operation creates a `Book` instance with the title **"1984"**, author **"George Orwell"**, and publication year **1949** using Django's ORM in the shell.

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984>
