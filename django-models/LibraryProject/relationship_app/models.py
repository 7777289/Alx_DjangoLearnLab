from django.db import models

# Many-to-One: A Library can have many Books
class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Libraries"


# Author model for Many-to-Many and One-to-One
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


# One-to-One: Each Author has one Profile
class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    biography = models.TextField()

    def __str__(self):
        return f"Profile of {self.author.name}"

    class Meta:
        verbose_name_plural = "Profiles"


# Many-to-Many: A Book can have many Authors, an Author can write many Books
# Many-to-One: Each Book belongs to one Library
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title


# Dummy test model (optional, for debugging)
class TestModel(models.Model):
    name = models.CharField(max_length=50)
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.library.name})"
