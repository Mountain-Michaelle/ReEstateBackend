from django.urls import path    
from .views import ListingsView, ListDetails, HomePageSearchView, ListingPageSearchView, ImageListView

urlpatterns = [
    path("search/", ListingsView.as_view()),
    path("detail/<str:slug>/", ListDetails.as_view()), 
    path('', HomePageSearchView.as_view()),
    path('listing-search/', ListingPageSearchView.as_view()),
    path('post-images/<slug:slug>/', ImageListView.as_view())
]
