from django.shortcuts import render
from .models import User
# Create your views here.
def index(request):
    user_list = User.objects.order_by('name')
    return render(request, 'users/user_list.html', {'user_list': user_list})

def user_detail(request, user_name):
    user = User.objects.get(name=user_name)
    return render(request, 'users/user_detail.html', {'user':user})
