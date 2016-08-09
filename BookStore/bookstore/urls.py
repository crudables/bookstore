from django.conf.urls import url
from . import  views
from BookStore import settings

urlpatterns = [
    url(r'^$', views.all_books,name='post_list'),
    
url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
               ]