from django.urls import path 
from .views import ContactCreateView

urlpatterns = [
    #Some url patterns
    path('', ContactCreateView.as_view())
]
