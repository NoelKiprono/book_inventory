from django.shortcuts import get_object_or_404, redirect, render 

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

         #   delete-book/34
def delete_book(request, id):
    book = Book.objects.get(id=id)                 # select * from books where id = 34
    book.delete()                       # delete from books where id= 34
    return redirect('show_books') 

def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BooksForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show_books')
    else:
        form = BooksForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})    




  

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
