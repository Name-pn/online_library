from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiRequest
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


# Create your views here.
class MyPagination(PageNumberPagination):
    page_size = 2  # Задаем размер страницы, по умолчанию 10

    def get_paginated_response(self, data):
        total_count = self.page.paginator.count
        num_pages = int(total_count / self.page_size) if total_count % self.page_size == 0 else int(total_count / self.page_size) + 1
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': total_count,
            'pages': num_pages,
            'results': data
        })
class AuthorViewSet(viewsets.ViewSet):
    mypagination_class = MyPagination()
    serializer_class = AuthorSerializer
    @extend_schema(
        tags=['Get'],
        summary="Получение автора по UUID",
    )
    def retrieve(self, request, pk=None):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author, many=False)
        return Response(serializer.data)

    @extend_schema(
        tags=['Get'],
        summary="Получение страницы с авторами",
        parameters=[
            OpenApiParameter(name='page', location=OpenApiParameter.QUERY, description='Номер страницы',
                             required=False, type=int),
            OpenApiParameter(name='name', location=OpenApiParameter.QUERY, description='Фильтр по имени автора',
                             required=False, type=OpenApiTypes.STR),
        ],
    )
    def list(self, request):
        queryset = Author.objects.all().order_by('title')
        if request.query_params.get('name'):
            filter_value = request.query_params.get('name')
            queryset = queryset.filter(Q(title__icontains=filter_value)
                                       | Q(title__startswith=filter_value))
        page = self.mypagination_class.paginate_queryset(queryset, request)
        serializer = AuthorSerializer(page, many=True)
        resp = self.mypagination_class.get_paginated_response(serializer.data)
        return resp

    @extend_schema(
        tags=['Post'],
        summary="Добавление автора",
        request=AuthorSerializer
    )
    def create(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=['Delete'],
        summary="Удаление автора по UUID",
    )
    def destroy(self, request, pk=None):
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        tags=['Put'],
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
        tags=['Get'],
        summary="Получение книги по UUID",
    )
    def retrieve(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data)

    @extend_schema(
        tags=['Get'],
        summary="Получение страницы с книгами",
        parameters=[
            OpenApiParameter(name='page', location=OpenApiParameter.QUERY, description='Номер страницы',
                             required=False, type=int),
            OpenApiParameter(name='name', location=OpenApiParameter.QUERY, description='Поиск по названию книги',
                             required=False, type=OpenApiTypes.STR),
        ],
    )
    def list(self, request):
        queryset = Book.objects.all().order_by('title')
        if request.query_params.get('name'):
            filter_value = request.query_params.get('name')
            queryset = queryset.filter(Q(title__icontains=filter_value)
                                       | Q(title__startswith=filter_value))
        p = self.mypagination_class.paginate_queryset(queryset, request)
        serializer = BookSerializer(p, many=True)
        resp = self.mypagination_class.get_paginated_response(serializer.data)
        return resp

    @extend_schema(
        tags=['Post'],
        summary="Добавление книги",
    )
    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=['Delete'],
        summary="Удаление книги по UUID",
    )
    def destroy(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(
        tags=['Put'],
        summary="Модификация книги по UUID",
        request=BookSerializer
    )
    def update(self, request, pk=None):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)