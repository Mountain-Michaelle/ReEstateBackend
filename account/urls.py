from django.urls import path 
from .views import SignUpView, CheckAuthenticated

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), ),
    path('is-authenticated/', CheckAuthenticated.as_view()),
]
