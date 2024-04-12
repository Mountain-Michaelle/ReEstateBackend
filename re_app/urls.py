from django.urls import path    
from .views import ListingsView, ListingView, HomePageSearchView, ListingPageSearchView

urlpatterns = [
    path("", ListingsView.as_view()),
    path("<str:slug>/", ListingView.as_view()), 
    path('search/', HomePageSearchView.as_view()),
    path('listing-search/', ListingPageSearchView.as_view())
]
