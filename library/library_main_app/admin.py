from django.contrib import admin
from .models import Book, Author, Genre


class BookAdmin(admin.ModelAdmin):
    ordering = ('title',)
    search_fields = ['title']
    list_per_page = 10


class AuthorAdmin(admin.ModelAdmin):
    ordering = ('title',)
    search_fields = ['title']
    list_per_page = 10


class GenreAdmin(admin.ModelAdmin):
    ordering = ('title',)
    search_fields = ['title']
    list_per_page = 10


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
