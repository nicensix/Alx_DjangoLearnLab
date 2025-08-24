from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm   # Import Django form for validation

# View books
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Create book
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Safe creation, avoids SQL injection
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, 'bookshelf/create_book.html', {"form": form})

# Edit book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # Safe update
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {"form": form, "book": book})

# Delete book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":  # Prevent accidental deletes via GET
        book.delete()
        return redirect("book_list")
    return render(request, 'bookshelf/delete_book.html', {"book": book})
