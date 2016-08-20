from django.conf.urls import url
from . import  views
#from BookStore import settings
from django.conf import settings

urlpatterns = [
    url(r'^$', views.all_books,name='all_books'),
    
url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
               ]