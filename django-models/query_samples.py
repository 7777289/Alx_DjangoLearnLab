# relationship_app/query_samples.py

import os
import django

# This line is crucial for setting up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings') 
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    """
    Function to demonstrate various model queries.
    """
    print("--- Sample Queries ---")

    # Clean up previous data for a fresh start
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # Create sample data
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George Orwell")

    book1 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author1)
    book2 = Book.objects.create(title="1984", author=author2)
    book3 = Book.objects.create(title="Animal Farm", author=author2)

    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="Community Library")

    # Add books to libraries (using the ManyToMany relationship)
    library1.books.add(book1, book2)
    library2.books.add(book3)
    library2.books.add(book2)

    librarian1 = Librarian.objects.create(name="Jane Doe", library=library1)
    librarian2 = Librarian.objects.create(name="John Smith", library=library2)
    
    # -----------------------------------------------------------
    # Query 1: Query all books by a specific author (ForeignKey)
    # -----------------------------------------------------------
    print("\n1. All books by George Orwell:")
    books_by_orwell = Book.objects.filter(author__name="George Orwell")
    for book in books_by_orwell:
        print(f"- {book.title}")

    # -----------------------------------------------------------
    # Query 2: List all books in a library (ManyToMany)
    # -----------------------------------------------------------
    print("\n2. All books in the Central Library:")
    # Retrieve the library object first
    central_library = Library.objects.get(name="Central Library")
    
    # Access the related books using the `books` attribute
    books_in_central_library = central_library.books.all()
    for book in books_in_central_library:
        print(f"- {book.title}")

    # -----------------------------------------------------------
    # Query 3: Retrieve the librarian for a library (OneToOne)
    # -----------------------------------------------------------
    print("\n3. Librarian for the Community Library:")
    # Retrieve the library object
    community_library = Library.objects.get(name="Community Library")

    # Access the related librarian using the reverse relationship
    # The default reverse name is the model name in lowercase.
    try:
        librarian = community_library.librarian
        print(f"- The librarian is: {librarian.name}")
    except Librarian.DoesNotExist:
        print("- No librarian found for this library.")

if __name__ == "__main__":
    run_queries()