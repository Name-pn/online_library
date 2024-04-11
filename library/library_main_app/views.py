from django.db.models import Q
from django.shortcuts import get_object_or_404
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Author, Book, Genre
from .serializers import AuthorSerializer, BookSerializer, GenreSerializer


# Create your views here.
class MyPagination(PageNumberPagination):
    page_size = 2  # Задаем размер страницы, по умолчанию 10

    def get_paginated_response(self, data):
        total_count = self.page.paginator.count
        num_pages = (
            int(total_count / self.page_size)
            if total_count % self.page_size == 0
            else int(total_count / self.page_size) + 1
        )
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "count": total_count,
                "pages": num_pages,
                "results": data,
            }
        )


class AuthorViewSet(viewsets.ViewSet):
    mypagination_class = MyPagination()
    serializer_class = AuthorSerializer

    @extend_schema(
        tags=["Автор"],
        summary="Получение автора по UUID",
    )
    def retrieve(self, request, pk=None):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author, many=False)
        return Response(serializer.data)

    @extend_schema(
        tags=["Автор"],
        summary="Получение страницы с авторами",
        parameters=[
            OpenApiParameter(
                name="page",
                location=OpenApiParameter.QUERY,
                description="Номер страницы",
                required=False,
                type=int,
            ),
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
        queryset = Author.objects.all().order_by("title")
        if request.query_params.get("name"):
            filter_value = request.query_params.get("name")
            queryset = queryset.filter(
                Q(title__icontains=filter_value) | Q(title__startswith=filter_value)
            )
        page = self.mypagination_class.paginate_queryset(queryset, request)
        serializer = AuthorSerializer(page, many=True)
        resp = self.mypagination_class.get_paginated_response(serializer.data)
        return resp

    @extend_schema(
        tags=["Автор"], summary="Добавление автора", request=AuthorSerializer
    )
    def create(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(tags=["Автор"], summary="Удаление автора по UUID")
    def destroy(self, request, pk=None):
        uuid = pk
        if not uuid:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            author = Author.objects.get(id=uuid)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        tags=["Автор"],
        summary="Модификация автора по UUID",
        request=AuthorSerializer,
    )
    def update(self, request, pk=None):
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookViewSet(viewsets.ViewSet):
    mypagination_class = MyPagination()
    serializer_class = BookSerializer

    @extend_schema(
        tags=["Книга"],
        summary="Получение книги по UUID",
    )
    def retrieve(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data)

    @extend_schema(
        tags=["Книга"],
        summary="Получение страницы с книгами",
        parameters=[
            OpenApiParameter(
                name="page",
                location=OpenApiParameter.QUERY,
                description="Номер страницы",
                required=False,
                type=int,
            ),
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
        queryset = Book.objects.all().order_by("title")
        if request.query_params.get("name"):
            filter_value = request.query_params.get("name")
            queryset = queryset.filter(
                Q(title__icontains=filter_value) | Q(title__startswith=filter_value)
            )
        p = self.mypagination_class.paginate_queryset(queryset, request)
        serializer = BookSerializer(p, many=True)
        resp = self.mypagination_class.get_paginated_response(serializer.data)
        return resp

    @extend_schema(
        tags=["Книга"],
        summary="Добавление книги",
    )
    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Книга"],
        summary="Удаление книги по UUID",
    )
    def destroy(self, request, pk=None):
        uuid = pk
        if not uuid:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            author = Book.objects.get(id=uuid)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        tags=["Книга"], summary="Модификация книги по UUID", request=BookSerializer
    )
    def update(self, request, pk=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreViewSet(viewsets.ViewSet):
    mypagination_class = MyPagination()
    serializer_class = GenreSerializer

    @extend_schema(
        tags=["Жанр"],
        summary="Получение жанра по UUID",
    )
    def retrieve(self, request, pk=None):
        genre = get_object_or_404(Genre, pk=pk)
        serializer = BookSerializer(genre, many=False)
        return Response(serializer.data)

    @extend_schema(
        tags=["Жанр"],
        summary="Получение жанров с их представителями",
        parameters=[
            OpenApiParameter(
                name="page",
                location=OpenApiParameter.QUERY,
                description="Номер страницы",
                required=False,
                type=int,
            ),
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
        queryset = Genre.objects.all().order_by("title")
        if request.query_params.get("name"):
            filter_value = request.query_params.get("name")
            queryset = queryset.filter(
                Q(title__icontains=filter_value) | Q(title__startswith=filter_value)
            )
        p = self.mypagination_class.paginate_queryset(queryset, request)
        serializer = GenreSerializer(p, many=True)
        resp = self.mypagination_class.get_paginated_response(serializer.data)
        return resp

    @extend_schema(
        tags=["Жанр"],
        summary="Добавление жанра",
    )
    def create(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Жанр"],
        summary="Удаление жанра по UUID",
    )
    def destroy(self, request, pk=None):
        uuid = pk
        if not uuid:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            author = Genre.objects.get(uuid=uuid)
        except Genre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        tags=["Жанр"], summary="Модификация жанра по UUID", request=BookSerializer
    )
    def update(self, request, pk=None):
        queryset = Genre.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = GenreSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
