from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from users.models import User
# Create your views here.

from .models import Book

def index(request):
    book_list = Book.objects.order_by('-publish_date')[:5]
    return render(request, 'books/book_list.html', {'book_list':book_list})

def book_detail(request, book_title):
    book = Book.objects.get(title=book_title)
    if request.method == 'POST':
        #貸し出しリクエストに必要な変数
        owner_name = book.owner
        borrower_name = "今ログインしている人"
        owner_email = User.objects.get(name= owner_name).email

        subject = "メール貸出リクエスト"
        message = "こんにちは！\n\n{0}さんが{1}さんの【{2}】を貸してほしいそうです。"\
        .format(borrower_name,owner_name,book)
        from_email = "loginner_email@gmail.com"
        recipient_list = [
            owner_email
        ]
        send_mail(subject, message, from_email, recipient_list,)
    return render(request, 'books/book_detail.html', {'book':book})
