from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

# from rest_framework_jwt.authentication import 

from .serializer import AccountSerializer, UserLoginSerializer, UserCreateSerializer

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
JWT_DECODE_HANDLER = api_settings.JWT_DECODE_HANDLER

class Register(viewsets.ViewSet):
    def create(self, request, pk=None):
        serializer = UserCreateSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)

        if User.objects.filter(username=serializer.validated_data['username']).first() is None:
            serializer.save()
            return Response({"message": "ok"}, status=status.HTTP_201_CREATED)
        return Response({"message": "duplicate username"}, status=status.HTTP_409_CONFLICT)

    

class Login(viewsets.ViewSet):
    def create(self, request, id=None):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
            
        if serializer.validated_data['username'] == "None":
            return Response({'message': 'fail'}, status=status.HTTP_200_OK)

        response = {
            'success': 'True',
            'token': serializer.data['token'],
        }
        return Response(response, status=status.HTTP_200_OK)


class AccountList(viewsets.ViewSet):
    
    def list(self, request, id=None):
        queryset = User.objects.all()
        serializer = AccountSerializer(queryset, many=True)
        
        return Response(serializer.data)
    
    def retrieve(self, request, id=None):
        user = get_object_or_404(User, id=id)
        serializer = AccountSerializer(user)
        
        return Response(serializer.data)

class CustomAuthToken(viewsets.ViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    
    def retrieve(self, request):
        # print(JWT_DECODE_HANDLER(request.headers['Authorization'].split()[-1]))
        print(request.user)
        return Response({'token': 1})
# Create your views here.
