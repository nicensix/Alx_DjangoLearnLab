from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for ListAPIView (read-only list)
    path('books/', BookList.as_view(), name='book-list'),

    # Router URLs (CRUD operations)
    path('', include(router.urls)),
]
