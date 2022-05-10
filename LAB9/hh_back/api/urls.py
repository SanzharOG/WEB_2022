from   django.contrib import admin 
from   django.urls   import path, include 
from . import   views 
urlpatterns  =  [ 
       path ( 'authors' ,  views.authorList ), 
       path ( 'authors/<int:id>' ,  views.authorDetail ),
       path ( 'authors/<int:id>/articles' ,  views.authorByarticle ), 
]