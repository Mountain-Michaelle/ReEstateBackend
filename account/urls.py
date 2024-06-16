from django.urls import path 
from .views import SignUpView, CheckAuthenticated, UserProfileView, Logout
urlpatterns = [
    path('sign-up/', SignUpView.as_view(), ),
    path('is-authenticated/', CheckAuthenticated.as_view()),
    path('user/', UserProfileView.as_view()),
    path('logout/', Logout.as_view())
]
