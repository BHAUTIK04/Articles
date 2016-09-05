from Articles.models import Articles
from rest_framework.serializers import ModelSerializer

class ArticleCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Articles
        fields =['title', 'content', 'is_active']
    
    
class ArticleDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model = Articles
        fields =['is_active']
    

