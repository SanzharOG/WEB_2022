from   django.http   import   JsonResponse 
from   django.shortcuts   import   render 
from   django.views.decorators.csrf   import   csrf_exempt 
from  .models   import   Author ,  Article 
  
  
  # Create your views here. 
from .serializers import PostSerializer 
  
  
def   authorList (request): 
    if request.method == 'GET':
       authors   =   Author.objects.all () 
       serializer   =   PostSerializer ( authors ,  many = True ) 
       return   JsonResponse ( serializer.data ,  safe = False ) 
    elif request.method == "CREATE":
        authors.create()
        return   JsonResponse ({ 'message':'created'},  status = 204 )
  
@csrf_exempt 
def   authorDetail ( request ,  id ): 
       try: 
           author   =   Author.objects.get ( id = id ) 
       except   Author.DoesNotExist as e: 
           return   JsonResponse ({ 'message':str (e)},  status = 400 ) 
  
       if   request.method   ==   'GET' : 
           serializer   =   PostSerializer ( author ) 
           return   JsonResponse ( serializer.data ,  safe = False ) 
       elif   request.method   ==   "UPDATE" : 
           author.update () 
           return   JsonResponse ({ 'message':'Updated'},  status = 204 ) 
       elif   request.method   ==   "DELETE" : 
           author.delete()
           return   JsonResponse ({ 'message':'Deleted'},  status = 204 ) 
  
  
def   authorByarticle ( request ,  id ): 
       authors   =   Author.objects.filter ( article_id = id ) 
       serializer   =   PostSerializer ( authors ,  many = True ) 
       return   JsonResponse ( serializer.data ,  safe = False )