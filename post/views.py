from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import PostSerializer
from .models import Post

class PostViewset(viewsets.ViewSet):
    
    def create(self, request, id=None):
        title = request.POST.get('title')
        description = request.POST.get('description')
        post = Post(title=title, description=description)
        post.save()
        
        serializer = PostSerializer(post)
        
        return Response(serializer.data)
        
    def list(self, request, id=None):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        
        return Response(serializer.data)
    
class PostElementViewset(viewsets.ViewSet):
        
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
        
        post.delete()
        
        serializer = PostSerializer(post)
        
        return Response(serializer.data)
        
    
    
    
    
# Create your views here.
