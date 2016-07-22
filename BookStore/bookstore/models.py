from __future__ import unicode_literals

from django.db import models

class Book(models.Model):# Create your models here.
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    price = models.IntegerField(default=0.00)
    released_date = models.DateTimeField
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30)
    