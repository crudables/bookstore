from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Book(models.Model):# Create your models here.
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2,default=0.00)
    former_price = models.DecimalField(max_digits=5, decimal_places=2,default=0.00)
    released_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30)
    isbn = models.CharField(primary_key=True,max_length=15, default="0000000000")
    picture = models.ImageField(default="")
    about = models.TextField(default="No information provided for this book")
    language = models.CharField(max_length=20,default="English")
    