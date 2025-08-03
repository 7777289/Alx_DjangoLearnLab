from relationship_app.models import Author, Book, Profile

# 1. Create a new Author
author = Author.objects.create(name="Chinua Achebe")

# 2. Create a Book linked to the Author (ForeignKey)
book = Book.objects.create(title="Things Fall Apart", author=author)

# 3. Create a Profile for the Author (OneToOne)
profile = Profile.objects.create(author=author, biography="Nigerian novelist and poet.")

# 4. Add a co-author to the book (ManyToMany)
another_author = Author.objects.create(name="Wole Soyinka")
book.co_authors.add(another_author)

# 5. Print some outputs
print(f"Book: {book.title}")
print(f"Main Author: {book.author.name}")
print("Co-authors:")
for co_author in book.co_authors.all():
    print(f"- {co_author.name}")
