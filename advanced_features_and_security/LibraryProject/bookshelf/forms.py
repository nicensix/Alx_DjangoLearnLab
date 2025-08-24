# bookshelf/forms.py
from django import forms
from .models import Book

# Example form to show secure input handling
class ExampleForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )

# Secure form for creating and editing Book instances
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]
