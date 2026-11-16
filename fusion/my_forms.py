from django import forms 

from fusion.models import Book

# django forms


class BooksForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = ('title', 'category', 'isbn', 'cost', 'year', 'published')

          
        