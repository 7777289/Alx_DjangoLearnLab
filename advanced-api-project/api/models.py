from django.db import models

# Author model represents a writer who can have multiple books.
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's name

    def __str__(self):
        return self.name


# Book model represents a written work linked to an author.
class Book(models.Model):
    title = models.CharField(max_length=255)  # Title of the book
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    # related_name='books' allows reverse access: author.books.all()

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
