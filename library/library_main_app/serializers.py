from rest_framework import serializers

from .models import Author, Book, Genre
from .validators import TitleFieldValidator


class UuidSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(required=True)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    titleVal = TitleFieldValidator()

    class Meta:
        model = Book
        fields = ["id", "title", "authors"]

    def validate_title(self, value):
        return self.titleVal(value)


class GenreSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    titleVal = TitleFieldValidator()

    class Meta:
        model = Genre
        fields = ["id", "title", "books"]

    def validate_title(self, value):
        return self.titleVal(value)
