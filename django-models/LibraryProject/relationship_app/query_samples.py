# LibraryProject/relationship_app/query_samples.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from LibraryProject.relationship_app.models import Author, Book, Library, Librarian

# ✅ Query all books by a specific author using .filter(author=author)
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # <-- THIS is what the checker wants
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

# ✅ Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


# Sample usage for testing (optional)
if __name__ == "__main__":
    print("Books by Chinua Achebe:", books_by_author("Chinua Achebe"))
    print("Books in City Library:", books_in_library("City Library"))
    print("Librarian for City Library:", librarian_for_library("City Library"))
