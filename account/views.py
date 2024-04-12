from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
# Create your views here.
User = get_user_model()

class SignUpView(APIView):
    permission_classes = (permissions.AllowAny, )
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
        
        