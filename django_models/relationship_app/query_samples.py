# relationship_app/query_samples.py

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')  # Replace with your actual project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query: All books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
    except Author.DoesNotExist:
        return []

# Query: All books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# Query: Librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


# Sample usage
if __name__ == '__main__':
    print("Books by 'Chinua Achebe':", books_by_author("Chinua Achebe"))
    print("Books in 'City Library':", books_in_library("City Library"))
    librarian = librarian_for_library("City Library")
    print("Librarian for 'City Library':", librarian if librarian else "No librarian found")
