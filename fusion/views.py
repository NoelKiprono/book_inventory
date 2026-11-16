from django.shortcuts import redirect, render

from fusion.my_forms import BooksForm

from  fusion.models import Book

# Create your views here.



def show_books(request):
   books = Book.objects.all() # select * from books
   return render(request, 'show_books.html', {'books': books})


def create_book(request):
    if request.method == 'POST':
      form = BooksForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('show_books')
    else:
      form = BooksForm()  
    return render(request, 'add_book.html', {'form': form})    






 #Book.objects.create(title = "The Rational Male", 
     #                   cost = 1000,
      #                  isbn = "458984809048", 
     #                   published = True
    #                      )

   # Book.objects.create(title = "The Man of People", 
   #                     category = "fiction",
   #                     year = 2010, 
   #                     cost = 1300,
    #                    isbn = "45399020048", 
     #                   published = True
     #                     )
