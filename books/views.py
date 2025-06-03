from django.shortcuts import render, get_object_or_404



from .models import Author, Publisher, Book, Classification

# Create your views here.

def book_display(request):
    books = Book.objects.all()
    classifications = Classification.objects.all()
    return render(request, 'display_books.html', {"books":books, "classifications":classifications})
    
def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request,'book_detail.html', {"book":book})

def author_profile(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.books.all()
    return render(request, "author_profile.html", {"author":author, "books":books})

def display_classifications(request):
    classifications = Classification.objects.all()
    return render(request, 'display_classifications.html', {"classifications":classifications})

def classification_profile(request, pk):
    classification = get_object_or_404(Classification, pk=pk)
    books = classification.books.all()
    return render(request, 'classification_profile.html', {"classification":classification, "books":books})