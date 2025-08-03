# Create Operation

This guide demonstrates how to create a new `Book` instance in the Django shell using the `bookshelf` app.

## Step 1: Open the Django Shell

```bash
python3 manage.py shell
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

print(book)
# Create Operation

This guide demonstrates how to create a new `Book` instance using Django's shell and ORM.

## Step 1: Open the Django Shell

Run the following command in your terminal:

```bash
python3 manage.py shell
