from django.contrib import admin
from .models import Book
from bookstore.models import Category
from .models import Customer,Address


# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Address)