from django.test import SimpleTestCase
from django.urls import reverse, resolve

from library_main_app.views import BookViewSet, AuthorViewSet

class TestUrls(SimpleTestCase):
    def test_books_url_is_resolved(self):
        url = reverse('books')
        self.assertEqual(resolve(url).func.cls, BookViewSet)

    def test_authors_url_is_resolved(self):
        url = reverse('authors')
        self.assertEqual(resolve(url).func.cls, AuthorViewSet)