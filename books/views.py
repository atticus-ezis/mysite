from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


from .models import Author, Publisher, Book, Classification

# Create your views here.

@login_required
def book_display(request):
    books = Book.objects.all()
    classifications = Classification.objects.all()
    publishers = Publisher.objects.all()
    return render(request, 'display_books.html', {"books":books, "classifications":classifications, "publishers":publishers})

@login_required
def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request,'book_detail.html', {"book":book})

@login_required
def author_profile(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.books.all()
    return render(request, "author_profile.html", {"author":author, "books":books})

@login_required
def display_classifications(request):
    classifications = Classification.objects.all()
    return render(request, 'display_classifications.html', {"classifications":classifications})

@login_required
def classification_profile(request, pk):
    classification = get_object_or_404(Classification, pk=pk)
    books = classification.books.all()
    return render(request, 'classification_profile.html', {"classification":classification, "books":books})

def user_agent(request):
    values = list(request.META.items())
    values.sort()
    html = []
    for k, v in values:
        html.append(f"<tr><td>{k}</td><td>{v}</td></tr>")
    return HttpResponse(f"<table>{''.join(html)}</table>\n")

def search(request):
    errors = []
    if "query" in request.GET:
        query = request.GET["query"]
        # breakpoint()
        if not query:
            errors.append("Enter a search term.")
        elif len(query) > 20:
            errors.append("Please enter at most 20 characters")

        else:
            books = Book.objects.filter(title__icontains=query)
            return render(request,"search_results.html",{"books": books, "query": query},)
    return render(request, "search_form.html", {"errors": errors})

from django.http import HttpResponseRedirect
from .forms import ContactForm, AuthorForm

def contact(request):
    if request.method == "POST": # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            return HttpResponseRedirect("/thanks/")
    else:
        form = ContactForm() # An unbound form
    return render(request,"contact.html", {"form": form}
)


def create_author(request):
    form = AuthorForm()
    if request.method == "POST":
        form = AuthorForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/authors/")
    context = {"form": form}
    return render(request, "create_author.html", context)

@user_passes_test(lambda u: u.is_staff, login_url='/books/user/login')
def update_author(request, pk=None):
    author = get_object_or_404(Author, pk=pk)
    form = AuthorForm(instance=author)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/authors/")
    context = {"form": form}
    return render(request, "update_author.html", context)

def delete_author(request, pk=None):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        author.delete()
        return HttpResponseRedirect("/authors/")
    context = {}
    return render(request, "delete_author.html", context)

# Exercise 4 create search for publisher and 

from .forms import SearchForm

def search_publisher(request):
    if "query" in request.GET:
        # query = request.GET.get("query")
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            publishers = Publisher.objects.filter(name__icontains=query)
    else:
        form = SearchForm()
        publishers = []


    return render(request, 'search_publisher.html', {"form": form, "publishers":publishers})

from django.db.models import Q

def search_author(request):
    if "query" in request.GET:    
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            authors = Author.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
    else:
        form = SearchForm()
        authors = []
    return render(request, 'search_author.html', {"form":form, "authors":authors})

# create book add update delete 

from .forms import CreateBook


@user_passes_test(lambda u: u.is_staff, login_url='/books/user/login')
def create_book(request):
    object = 'Book'
    if request.method == 'POST':
        form = CreateBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_display')
    else:
        form = CreateBook()
    context = {"form":form, "object":object}
    return render(request, 'create_book.html', context)

def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = CreateBook(instance=book)
    if request.method == 'POST':
        form = CreateBook(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_display')
    return render(request, 'update_book.html', {"form":form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {'book':book}
    if request.method == 'POST':
        book.delete()
        return redirect('book_display')
    return render(request, "delete_author.html", context)
    
    
# publisher create, update, delete
from .forms import CreatePublisher

@user_passes_test(lambda u: u.is_staff, login_url='/books/user/login')
def create_publisher(request):
    object = 'Publisher'
    if request.method == 'POST':
        form = CreatePublisher(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_display')
    else:
        form = CreatePublisher()
    context = {'form':form, "object":object}
    return render(request, "create_book.html", context)

def update_publisher(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    form = CreatePublisher(instance=publisher)
    if request.method == 'POST':
        form = CreatePublisher(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('book_display')
    context = {"form":form, "publisher":publisher}
    return render(request, 'update_book.html', context)
    
def delete_publisher(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('book_display')
    return render(request, 'delete_author.html')

from .forms import UserRegister
from django.contrib.auth import login

def register_user(request):
    if request.method=='POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_display')
    form = UserRegister()
    return render(request, 'registration.html', {"form":form, "subject":"Signup"})

from .forms import UserLogin
from django.contrib.auth import authenticate

def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('book_display')
    form = UserLogin()
    return render(request, 'registration.html', {"form":form, "subject":"Login"})

from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('login_user')


