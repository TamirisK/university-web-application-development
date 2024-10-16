from django.shortcuts import render
from .models import Book, User, Order

def home(request):
    return render(request, 'home.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})