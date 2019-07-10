from django.shortcuts import render
from .models import User
from books.models import Book
# Create your views here.
def index(request):
    user_list = User.objects.order_by('name')
    return render(request, 'users/user_list.html', {'user_list': user_list})

def user_detail(request, user_name):
    user = User.objects.get(name=user_name)
    owning_books = Book.objects.filter(owner=user_name)
    borrowing_books = Book.objects.filter(borrower=user_name)
    context = {
        'user': user,
        'owning_books': [owning_book for owning_book in owning_books],
        'borrowing_books': [borrowing_book for borrowing_book in borrowing_books],
    }
    return render(request, 'users/user_detail.html', context)
