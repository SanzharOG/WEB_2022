from pydoc import describe
from django.db import models 
  
  
class   Author ( models.Model ): 
       name   =   models.CharField ( max_length = 200 ) 
       email = models.CharField(max_length= 200)
       def   str (self): 
           return   self.name 
  
class   Article ( models.Model ): 
       title   =   models.CharField ( max_length = 200 ) 
       description   =   models.TextField () 
       author   =   models.ForeignKey ( Author ,  on_delete = models.CASCADE ) 
  
       def   str (self): 
           return   self.title