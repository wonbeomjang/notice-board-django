from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializer import PostSerializer
from .models import Post

class PostViewset(viewsets.ViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    
    def create(self, request, id=None):
        if request.user.is_anonymous:
            return Response({'message': 'token is needed'}, status=status.HTTP_401_UNAUTHORIZED)
        
        print(request.user)
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user
        post = Post(title=title, description=description, user=user)
        post.save()
        
        serializer = PostSerializer(post)
        
        return Response(serializer.data)
        
    def list(self, request, id=None):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        
        return Response(serializer.data)
    
class PostElementViewset(viewsets.ViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
        
    def retrieve(self, request, id=None):
        post = get_object_or_404(Post, id=id)
        serializer = PostSerializer(post)
        
        return Response(serializer.data)
        
    def update(self, request, id=None):
        post = get_object_or_404(Post, id=id)
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        if title:
            post.title = title
        if description:
            post.description = description
        
        post.save()
        serializer = PostSerializer(post)
        
        return Response(serializer.data)
    
    def destroy(self, request, id=None):
        post = get_object_or_404(Post, id=id)
        
        if post.user == request.user:
            post.delete()
            return Response({'message': 'ok'})
        
        return Response({'message': 'token is needed'}, status=status.HTTP_401_UNAUTHORIZED)
        
    
    
    
    
# Create your views here.
