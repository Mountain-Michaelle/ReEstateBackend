from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework import permissions
from rest_framework import status
from .models import ReAccountUser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import PermissionDenied
from rest_framework.authtoken.models import Token
from django.contrib import auth
# from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
# Create your views here.
User = get_user_model()

class SignUpView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        data = self.request.data
        name = data['name']
        email = data['email']
        phone = data['phone']
        password = data['password']
        re_password = data['re_password']
        
    
        if password == re_password:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Account email already exists'})
            
            else:
                if len(password) < 8:
                    return Response({'error': 'Password must be at least 8 characters'})
                else:
                    user = User.objects.create_user(name=name, email=email, phone=phone, password=password)
                    
                    user.save()
                    return Response({'success': 'Account created successfully!'})
        else:
            Response({'error': 'Passwords do not match'})


class CheckAuthenticated(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    
    try:
        def post(self, request, format=None):
            user = self.request.user
            if user.is_authenticated:
                return Response({'isAuthenticated': True}, status=status.HTTP_200_OK)
            
            return Response({'error': 'Unauthorized request', 'isAuthenticated': False}, status.HTTP_401_UNAUTHORIZED)
    except:
        Response({"error": "Something went wrong"})
        
    

class Logout(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def post(self, request, format=None):
        # try:

        token = request.auth
        if isinstance(token, Token):
            token.delete()
            return Response({"success": "You are logged out successfully"}, status=status.HTTP_200_OK)
        
        else:
            return Response("Good one!")
        
        # except:
        #     return Respons


class UserProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    def post(self, request, format=None):
        user = self.request.user
        id = user.id
        email = user.email,
        name = user.name
        print("what is happening ", user.is_authenticated)
        return Response({"email": email, "name": str(name), "id": id})
        
            
    