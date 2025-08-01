# Update Operation

This operation updates the title of the book from `"1984"` to `"Nineteen Eighty-Four"`.

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
# <Book: Nineteen Eighty-Four>
