from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication(self, value):
        if value > 2024:
           raise serializers.ValidationError("The publication year cannot be greater than the current year")
        return value
    

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name']

# The book and author models establish a one-to-many relationship.
# The validation function checks if the publication year is not in the future.