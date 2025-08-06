# relationship_app/query_samples.py
import os
import django
import sys

# Set up Django environment
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    """Create test data for demonstration"""
    # Clear existing data
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # Create authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George R.R. Martin")

    # Create books
    book1 = Book.objects.create(title="Harry Potter 1", author=author1)
    book2 = Book.objects.create(title="Harry Potter 2", author=author1)
    book3 = Book.objects.create(title="A Game of Thrones", author=author2)

    # Create library
    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2, book3)

    # Create librarian
    Librarian.objects.create(name="Sarah Johnson", library=library)

def demonstrate_queries():
    """Show example queries for each relationship type"""
    # 1. ForeignKey query: Get all books by an author
    print("\nBooks by J.K. Rowling:")
    for book in Book.objects.filter(author__name="J.K. Rowling"):
        print(f"- {book.title}")

    # 2. ManyToMany query: Get all books in a library
    print("\nBooks in Central Library:")
    library = Library.objects.get(name="Central Library")
    for book in library.books.all():
        print(f"- {book.title} (by {book.author.name})")

    # 3. OneToOne query: Get librarian for a library
    print("\nLibrarian for Central Library:")
    librarian = Librarian.objects.get(library__name="Central Library")
    print(f"{librarian.name} manages {librarian.library.name}")

def main():
    create_sample_data()
    demonstrate_queries()

if __name__ == "__main__":
    main()