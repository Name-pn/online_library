import uuid

from django.test import Client, TestCase
from django.urls import reverse
from library_main_app.models import Author, Book


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.books_url = reverse("books")
        self.author_url = reverse("authors")

        self.book_uuid = uuid.uuid4()
        self.book1 = Book.objects.create(
            title="Test book",
            id=self.book_uuid,
        )

        self.author_uuid = uuid.uuid4()
        self.author1 = Author.objects.create(
            title="Test author",
            id=self.author_uuid,
        )

        self.book_detail_url = reverse("book_by_uuid", args=[str(self.book_uuid)])
        self.author_detail_url = reverse("author_by_uuid", args=[str(self.author_uuid)])

    def test_books_page_GET(self):
        response = self.client.get(self.books_url)
        self.assertEqual(response.status_code, 200)

    def test_authors_page_GET(self):
        response = self.client.get(self.author_url)
        self.assertEqual(response.status_code, 200)

    def test_book_detail_GET(self):
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, 200)

    def test_author_detail_GET(self):
        response = self.client.get(self.author_detail_url)
        self.assertEqual(response.status_code, 200)

    def test_book_POST(self):
        pre_count = Book.objects.count()
        response = self.client.post(
            self.books_url,
            {
                "title": "POST book title",
            },
        )
        self.assertEqual(response.status_code, 201)
        post_count = Book.objects.count()
        self.assertEqual(post_count, pre_count + 1)

    def test_author_POST(self):
        pre_count = Author.objects.count()
        response = self.client.post(
            self.author_url,
            {
                "title": "POST author title",
            },
        )
        self.assertEqual(response.status_code, 201)
        post_count = Author.objects.count()
        self.assertEqual(post_count, pre_count + 1)

    def test_book_DELETE(self):
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, 204)
        # Проверяем, что автор был успешно удален
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=self.book_uuid)

    def test_author_DELETE(self):
        response = self.client.delete(self.author_detail_url)
        self.assertEqual(response.status_code, 204)
        with self.assertRaises(Author.DoesNotExist):
            Author.objects.get(id=self.author_uuid)

    def test_book_PUT(self):
        response = self.client.put(
            self.book_detail_url,
            {"title": "PUT book title UPDATED"},
            format="json",
            content_type="application/json",
        )
        data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Book.objects.get(id=self.book_uuid).title, data["title"])

    def test_author_PUT(self):
        response = self.client.put(
            self.author_detail_url,
            {"title": "PUT author title"},
            format="json",
            content_type="application/json",
        )
        data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Author.objects.get(id=self.author_uuid).title, data["title"])

    def test_book_search_GET(self):
        response = self.client.get(self.books_url, {"name": "Test book"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

        response = self.client.get(self.books_url, {"name": "Not exist book"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 0)

    def test_author_search_GET(self):
        response = self.client.get(self.author_url, {"name": "Test author"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

        response = self.client.get(self.author_url, {"name": "Not exist author"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 0)
