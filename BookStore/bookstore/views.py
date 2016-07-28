from django.shortcuts import render
from .models import  Book

# Create your views here.
def post_list(request):
    books = Book.objects.all()
    return render(request,'bookstore/homepage.html',{'books':books})