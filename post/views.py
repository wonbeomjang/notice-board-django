from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializer import PostSerializer
from .models import Post
from .pagination import PostPageNumberPagination

class PostViewset(viewsets.ModelViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # pagination_class = PostPageNumberPagination
    
    def create(self, request, id=None):
        if request.user.is_anonymous:
            return Response({'message': 'token is needed'}, status=status.HTTP_401_UNAUTHORIZED)
        
        print(request.user)
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user
        post = Post(title=title, description=description, user=user)
        post.save()
        
        SerializerClass = self.get_serializer_class()
        serializer = SerializerClass(post)
        
        return Response(serializer.data)
    
class PostElementViewset(viewsets.ModelViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
    
    def update(self, request, id=None):
        post = get_object_or_404(Post, id=id)
        
        if request.user != post.user:
            return Response({'message': 'token is needed'}, status=status.HTTP_401_UNAUTHORIZED)
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        if title:
            post.title = title
        if description:
            post.description = description
        
        post.save()
        SerializerClass = self.get_serializer_class()
        serializer = SerializerClass(post)
        
        return Response(serializer.data)
    
    
# Create your views here.
