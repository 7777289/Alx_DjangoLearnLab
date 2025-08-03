from .models import Author, Book, Library

def run_queries():
    print("📚 Authors:")
    for author in Author.objects.all():
        print(f"- {author.name}")

    print("\n📘 Books and their Authors:")
    for book in Book.objects.select_related('author').all():
        print(f"- {book.title} by {book.author.name}")

    print("\n🏛️ Libraries and their Books:")
    for library in Library.objects.prefetch_related('books').all():
        print(f"- {library.name}:")
        for book in library.books.all():
            print(f"  • {book.title}")

    print("\n✅ Query samples completed.")

