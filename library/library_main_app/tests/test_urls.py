from django.test import SimpleTestCase
from django.urls import resolve
from library_main_app.views import AuthorViewSet, BookViewSet
from rest_framework.reverse import reverse


class TestUrls(SimpleTestCase):

    def test_books_url_is_resolved(self):
        url = reverse("books")
        self.assertEqual(resolve(url).func.cls, BookViewSet)

    def test_authors_url_is_resolved(self):
        url = reverse("authors")
        self.assertEqual(resolve(url).func.cls, AuthorViewSet)
