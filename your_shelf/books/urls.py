from django.urls import path
from . import views

app_name='books'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:book_title>/', views.book_detail, name='book_detail'),
]
