from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, publication_year):
        if publication_year > (publication_year + 1):
           raise serializers.ValidationError("The publication year cannot be greater than the current year")
        return publication_year
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name']

# The book and author models establish a one-to-many relationship.