from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import BookViewSet, AuthorViewSet

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('books/', BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='books'),
    path('books/<uuid:pk>', BookViewSet.as_view({'delete': 'destroy', 'put': 'update', 'get': 'getOne'}), name='book_by_uuid'),
    path('authors/', AuthorViewSet.as_view({'get': 'list', 'post': 'create'}), name='authors'),
    path('authors/<uuid:pk>', AuthorViewSet.as_view({'delete': 'destroy', 'put': 'update', 'get': 'getOne'}), name='author_by_uuid'),
]