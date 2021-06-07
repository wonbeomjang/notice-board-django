from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import models

from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import AccountSerializer

class Register(viewsets.ViewSet):
    def create(self, request, pk=None):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email    = request.POST.get('email')
        
        user = models.User.objects.filter(username=username).count()
        if user:
            return Response({'message': 'duplicated username'})
        
        user = models.User(username=username, email=email)
        user.set_password(password)
        user.save()
        
        serializer = AccountSerializer(user)
        
        return Response(serializer.data)

    

class Login(viewsets.ViewSet):
    def retrieve(self, request, id=None):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = models.User.objects.filter(username=username).count()

        if not user:
            return Response({'message': 'fail'})
            
        user = models.User.objects.get(username=username)
        check = user.check_password(password)
        
        if check:
            return Response({'message': 'success'})
        else:
            return Response({'message': 'fail'})


class AccountList(viewsets.ViewSet):
    
    def list(self, request, id=None):
        queryset = models.User.objects.all()
        serializer = AccountSerializer(queryset, many=True)
        
        return Response(serializer.data)
    
    def retrieve(self, request, id=None):
        user = get_object_or_404(models.User, id=id)
        serializer = AccountSerializer(user)
        
        return Response(serializer.data)

# Create your views here.
