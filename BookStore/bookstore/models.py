from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from BookStore import settings


class Category(models.Model):
    name = models.CharField(max_length=50,unique =True)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default = True)
    meta_keywords = models.CharField('Meta Keywords',max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag', default='meta-keyword for category')
    meta_description = models.CharField("Meta Description", max_length=255,help_text='Content for description meta tag',default='meta-description for category')
    
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
    image = models.ImageField(upload_to=settings.MEDIA_ROOT)
    about = models.TextField(default="No information provided for this book")
    language = models.CharField(max_length=20,default="English")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField(default=0)
#     slug = models.SlugField(max_length=50,unique=True, help_text="Unique value for product url, created from name",default="No slug provided for book")
    slug = models.CharField(max_length=200,editable = False)
    meta_keywords = models.CharField('Meta Keywords',max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag', default='Meta_keyword for book')
    meta_description = models.CharField("Meta Description", max_length=255,help_text='Content for description meta tag',default='meta_description for book')
    
    class Meta:
        db_table = 'Books'
        ordering = ['-created_at']
        
        def __unicode__(self):
            return self.name
        
#         @models.permalink
#         def get_absolute_url(self):
#             return ('catalog_category',(),{'category_slug':self.slug})
        
#         def sale_price(self):
#             if self.old_price > self.price:
#                 return self.price
#             else:
#                 return None
            
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.title)
        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)  
    
    
class Address(models.Model):
    email = models.CharField(max_length=50)
    home_phone = models.CharField(max_length=13)
    mobile_phone = models.CharField(max_length=13)
    home_Add = models.CharField(max_length=150)
    office_add = models.CharField(max_length=150)
    slug = models.SlugField(max_length=50, unique=True, help_text="Unique value for product url, created from name",default="No slug provided for address")
        
    
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    address =  models.ManyToManyField(Address)
    
    