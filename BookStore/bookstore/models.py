from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50,unique =True)
    created_at=models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)
    meta_keywords = models.CharField('Meta Keywords',max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length=255,help_text='Content for description meta tag')
    
    class Meta:
        db_table = 'Categories'
        ordering = ['-created_at']
        verbose_name = 'Categories'
        
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('catalog_category',(),{'category_slug':self.slug})

class Book(models.Model):# Create your models here.
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2,default=0.00)
    active = models.BooleanField(default=False)
    old_price = models.DecimalField(max_digits=5, decimal_places=2,default=0.00,blank=True)
    released_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    isbn = models.CharField(primary_key=True,max_length=15, default="0000000000")
    image = models.ImageField(default="")
    about = models.TextField(default="No information provided for this book")
    language = models.CharField(max_length=20,default="English")
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField(default=0)
    slug = models.SlugField(max_length=50, unique=True, help_text="Unique value for product url, created from name")
    meta_keywords = models.CharField('Meta Keywords',max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length=255,help_text='Content for description meta tag')
    
    class Meta:
        db_table = 'Book'
        ordering = ['-created']
        
        def __unicode__(self):
            return self.name
        
        @models.permalink
        def get_absolute_url(self):
            return ('catalog_product', (), {'product_slug':self.slug})
        
        def sale_price(self):
            if self.old_price > self.price:
                return self.price
            else:
                return None
            
            
    
    
class Address(models.Model):
    email = models.CharField(max_length=50)
    home_phone = models.CharField(max_length=13)
    mobile_phone = models.CharField(max_length=13)
    home_Add = models.CharField(max_length=150)
    office_add = models.CharField(max_length=150)
    slug = models.SlugField(max_length=50, unique=True, help_text="Unique value for product url, created from name")
        
    
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    address =  models.ManyToManyField(Address)
    
    