from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    biography = models.TextField()

    def __str__(self):
        return f"Profile of {self.author.name}"

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='main_books')
    co_authors = models.ManyToManyField(Author, related_name='coauthored_books', blank=True)

    def __str__(self):
        return self.title
