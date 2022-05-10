from   rest_framework   import  serializers 
  
from  .models   import   Author ,  Article 
  
  
class   PostSerializer ( serializers . ModelSerializer ): 
       name = serializers.CharField(read_only=True) 
       #email = PostSerializer() 
       class   Meta : 
           model   =  Author
           fields   =  ( 'id' ,  'name' ,  'email' ) 
           read_only_fields = ('name',)
           
def create(self, validated_data):
        author = Author.objects.create(name=validated_data['name'], email=validated_data['email'])
        return author

def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.email = validated_data['email']
        instance.save()
        return instance
