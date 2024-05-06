from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.response import Response
from .models import Contact
# Create your views here.

class ContactCreateView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format=None):
        data = self.request.data
        subject = data['subject']
        name = data['name']
        email = data['email']
        message = data['message']
        phone = data['phone']
        
        msg_mail = f'Name: {name}\n \nEmail: {email}\n \nMessage: \n\t{message}\n Phone: {phone}\n '
    
    # try:
        send_mail(
            subject,
            msg_mail,
            'debees24@gmail.com',
            ['debees24@gmail.com'],
            fail_silently=False
            
        )
        
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        
        return Response({'success': 'Thank you!, Your mesage was sent successfully'})
    
    # except:
    #     return Response({'Message failed to send'})