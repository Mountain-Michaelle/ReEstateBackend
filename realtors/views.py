from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions 
from .models import Realtors
from .serializers import RealtorSerializer

# Create your views here.

class RealtorListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Realtors.objects.all()
    serializer_class = RealtorSerializer
    pagination_class = None
    
    
class RealtorDetailView(RetrieveAPIView):
    queryset = Realtors.objects.all()
    serializer_class = RealtorSerializer
    
    
class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Realtors.objects.filter(top_seller=True)
    serializer_class = RealtorSerializer
    pagination_class = None