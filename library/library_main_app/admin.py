from django.contrib import admin
from .models import Book, Author
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    ordering = ('title',)
    search_fields = ['title']
    list_per_page = 10

class AuthorAdmin(admin.ModelAdmin):
    ordering = ('title',)
    search_fields = ['title']
    list_per_page = 10

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)