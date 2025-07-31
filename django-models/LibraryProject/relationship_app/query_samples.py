# LibraryProject/relationship_app/query_samples.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from LibraryProject.relationship_app.models import Author, Book, Library, Librarian

# ✅ Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # required pattern
        return books
    except Author.DoesNotExist:
        return []

# ✅ Query all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# ✅ Retrieve the librarian for a library using Librarian.objects.get(library=...)
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # <-- required pattern
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


# Sample usage (optional)
if __name__ == "__main__":
    print("Books by Chinua Achebe:", books_by_author("Chinua Achebe"))
    print("Books in City Library:", books_in_library("City Library"))
    print("Librarian for City Library:", librarian_for_library("City Library"))


# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
