# BookSerializer: Serializes all fields of the Book model
from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation to ensure the publication year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
# AuthorSerializer: Serializes the author and their related books using a nested serializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

    """
    Serializer for the Author model.

    This serializer handles the conversion of Author model instances to JSON format
    and vice versa. It includes a nested representation of the author's books.

    Fields:
    - id: Automatically included by ModelSerializer.
    - name: The author's name.
    - books: A nested serialization of all books by this author.

    The 'books' field uses the BookSerializer to provide a detailed representation
    of each book associated with the author. This creates a nested structure in
    the serialized data, allowing for a comprehensive view of an author and their works.
    """
