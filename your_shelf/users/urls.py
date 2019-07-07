from django.urls import path
from . import views

app_name='users'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:user_name>/', views.user_detail, name='user_detail'),
]
