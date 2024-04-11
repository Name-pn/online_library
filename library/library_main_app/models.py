import uuid

from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    title = models.CharField(max_length=255, unique=True)

    class Meta:
        app_label = "library_main_app"

    def __str__(self):
        return self.title


class Author(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    title = models.CharField(max_length=255, unique=True)
    books = models.ManyToManyField(Book, related_name="authors", blank=True)

    class Meta:
        app_label = "library_main_app"

    def __str__(self):
        return self.title


class Genre(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    books = models.ManyToManyField(Book, related_name="books_by_genre", blank=True)

    class Meta:
        app_label = "library_main_app"

    def __str__(self):
        return self.title
