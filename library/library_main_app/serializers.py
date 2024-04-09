from rest_framework import serializers
from .models import Author, Book
from .validators import UnknownFieldsValidator, TitleFieldValidator


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    titleVal = TitleFieldValidator()
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors']
    def validate_title(self, value):
        return self.titleVal(value)
