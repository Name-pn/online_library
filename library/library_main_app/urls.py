from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import BookViewSet, AuthorViewSet, GenreViewSet

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('books/', BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='books'),
    path('books/<uuid:pk>',
         BookViewSet.as_view(
             {'put': 'update', 'get': 'retrieve', 'delete': 'destroy'}
         ), name='book_by_uuid'),
    path('authors/', AuthorViewSet.as_view({'get': 'list', 'post': 'create'}), name='authors'),
    path('authors/<uuid:pk>',
         AuthorViewSet.as_view(
             {'put': 'update', 'get': 'retrieve', 'delete': 'destroy'}
         ), name='author_by_uuid'),
    path('genres/', GenreViewSet.as_view({'get': 'list', 'post': 'create'}), name='genres'),
    path('genres/<uuid:pk>',
         GenreViewSet.as_view(
             {'delete': 'destroy', 'put': 'update', 'get': 'retrieve'}
         ), name='genre_by_uuid'),
]
