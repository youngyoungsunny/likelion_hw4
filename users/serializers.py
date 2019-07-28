from rest_framework.serializers import ModelSerializer
from .models import CustomerUser, Post
from rest_framework.fields import ReadOnlyField

class UserSerializer(ModelSerializer):
    
    class Meta:
        model = CustomerUser
        fields = ['email', 'username']


class PostSerializer(ModelSerializer):
    author_username = ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'author_username', 'message','image']