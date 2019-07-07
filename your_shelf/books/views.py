from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Book

def index(request):
    book_list = Book.objects.order_by('-publish_date')[:5]
    return render(request, 'books/book_list.html', {'book_list':book_list})

def book_detail(request, book_title):
    book = Book.objects.get(title=book_title)
    return render(request, 'books/book_detail.html', {'book':book})
