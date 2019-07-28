from rest_framework import generics
from .serializers import UserSerializer, PostSerializer
from .models import CustomerUser, Post
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAuthorOrReadonly


class UserListView(generics.ListCreateAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = UserSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    permission_classes = [IsAuthorOrReadonly,]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)