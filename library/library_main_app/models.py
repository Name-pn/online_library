from django.db import models
import uuid
# Create your models here.
class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=255, unique=True)
    books = models.ManyToManyField(Book, related_name='authors', blank=True)
    def __str__(self):
        return self.title