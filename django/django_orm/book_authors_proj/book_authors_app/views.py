from django.shortcuts import render, redirect, HttpResponse
from .models import *

def index(request):
    context = {
        'book_title': Book.objects.all()
    }
    return render(request, 'index.html', context)

def index_authors(request):
    context = {
        'authors_title': Author.objects.all()
    }
    return render(request, 'authors.html', context)

def index_books(request, booksID):
    if request.method == 'POST':
        author_id = Author.objects.get(id=request.POST['author_id'])
        Book.objects.get(id=booksID).author.add(author_id)
    context = {
        'book_info': Book.objects.get(id=booksID),
        'authors_name': Author.objects.all()
    }
    return render(request, 'books.html', context)

def index_author_info(request, authorsID):
    if request.method == 'POST':
        book_id = Book.objects.get(id=request.POST['book_id'])
        Author.objects.get(id=authorsID).books.add(book_id)
    context = {
        'authors_info': Author.objects.get(id=authorsID),
        'books_name': Book.objects.all()
    }
    return render(request, 'authors_info.html', context)

def add_book(request):
    Book.objects.create(title=request.POST['title'],desc=request.POST['description'])
    return redirect('/')

def add_author(request):
    Author.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],notes=request.POST['notes'])
    return redirect('/authors')
