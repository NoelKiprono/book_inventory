from django.shortcuts import render

from fusion.models import Book

# Create your views here.



def show_books(request):
   books = Book.objects.all() # select * from books
   return render(request, 'show_books.html', {'books': books})


def create_book(request):
    Book.objects.create(title = "The Rational Male", 
                        category = "fiction", 
                        year = 2015, 
                        cost = 1000,
                        isbn = "458984809048", 
                        published = True
                          )

    Book.objects.create(title = "The Man of People", 
                        category = "fiction",
                        year = 2010, 
                        cost = 1300,
                        isbn = "45399020048", 
                        published = True
                          )

    return render(request, 'add_book.html')    

