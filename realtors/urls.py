from django.urls import path 
from .views import RealtorListView, RealtorDetailView, TopSellerView


urlpatterns = [
    path('realtor-list/', RealtorListView.as_view()),
    path('<int:pk>/', RealtorDetailView.as_view()),
    path('top-seller/', TopSellerView.as_view()),
]
