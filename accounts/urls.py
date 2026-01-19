from django.urls import path
from .views import UserRegistrationView, UserLoginView, BuyerProfileUpdateView, SellerProfileUpdateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('buyer/profile/', BuyerProfileUpdateView.as_view()),
    path('seller/profile/', SellerProfileUpdateView.as_view()),
]
