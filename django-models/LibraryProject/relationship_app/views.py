# LibraryProject/relationship_app/views.py

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # ✅ required import

# ✅ Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # ✅ required query
    return render(request, 'relationship_app/list_books.html', {'books': books})  # ✅ required path

# ✅ Class-based view to show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ required string
    context_object_name = 'library'  # ✅ required name
