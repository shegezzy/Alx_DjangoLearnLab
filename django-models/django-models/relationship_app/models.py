from django.db import models

class Author_Model(models.Model):
    name = models.CharField(max_length=200)

class Book_Model(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author_Model, on_delete=models.CASCADE, related_name='authors')

class Library_Model(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book_Model, on_delete=models.CASCADE, related_name='library' )

class Librarian_Model(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library_Model)
# Create your models here.
