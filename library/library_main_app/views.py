from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Author, Book, Genre
from .serializers import AuthorSerializer, BookSerializer, GenreSerializer


# Create your views here.
class MyPagination(PageNumberPagination):
    page_size = 2  # Задаем размер страницы, по умолчанию 2


class SearchMixin():
    def get_queryset(self):
        queryset = self.queryset
        name = self.request.query_params.get('name', '')
        if name:
            queryset = queryset.filter(title__icontains=name)
        return queryset

class AuthorViewSet(SearchMixin,
                    viewsets.ModelViewSet):
    pagination_class = MyPagination
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    @extend_schema(
        tags=["Автор"],
        summary="Получение автора по UUID",
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request)

    @extend_schema(
        tags=["Автор"],
        summary="Получение страницы с авторами",
        parameters=[
            OpenApiParameter(
                name="name",
                location=OpenApiParameter.QUERY,
                description="Фильтр по имени автора",
                required=False,
                type=OpenApiTypes.STR,
            ),
        ],
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        tags=["Автор"],
        summary="Добавление автора",
        request=AuthorSerializer
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        tags=["Автор"],
        summary="Удаление автора по UUID")
    def destroy(self, request, pk=None):
        return super().destroy(request)

    @extend_schema(
        tags=["Автор"],
        summary="Модификация автора по UUID",
        request=AuthorSerializer,
    )
    def update(self, request, pk=None):
        return super().update(request)

class BookViewSet(SearchMixin,
                  viewsets.ModelViewSet):
    pagination_class = MyPagination
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    @extend_schema(
        tags=["Книга"],
        summary="Получение книги по UUID",
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request)

    @extend_schema(
        tags=["Книга"],
        summary="Получение страницы с книгами",
        parameters=[
            OpenApiParameter(
                name="name",
                location=OpenApiParameter.QUERY,
                description="Поиск по названию книги",
                required=False,
                type=OpenApiTypes.STR,
            ),
        ],
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        tags=["Книга"],
        summary="Добавление книги",
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        tags=["Книга"],
        summary="Удаление книги по UUID",
    )
    def destroy(self, request, pk=None):
        return super().destroy(request)

    @extend_schema(
        tags=["Книга"], summary="Модификация книги по UUID", request=BookSerializer
    )
    def update(self, request, pk=None):
        return super().update(request)

class GenreViewSet(SearchMixin,
                   viewsets.ModelViewSet):
    pagination_class = MyPagination
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

    @extend_schema(
        tags=["Жанр"],
        summary="Получение жанра по UUID",
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request)

    @extend_schema(
        tags=["Жанр"],
        summary="Получение жанров с их представителями",
        parameters=[
            OpenApiParameter(
                name="name",
                location=OpenApiParameter.QUERY,
                description="Поиск по названию жанра",
                required=False,
                type=OpenApiTypes.STR,
            ),
        ],
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        tags=["Жанр"],
        summary="Добавление жанра",
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        tags=["Жанр"],
        summary="Удаление жанра по UUID",
    )
    def destroy(self, request, pk=None):
        return super().destroy(request)

    @extend_schema(
        tags=["Жанр"],
        summary="Модификация жанра по UUID",
        request=BookSerializer
    )
    def update(self, request, pk=None):
        return super().update(request)
