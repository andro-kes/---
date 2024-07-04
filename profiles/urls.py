from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import create_profile, create_profile_page



urlpatterns = [
    path('api/create_profile/', create_profile),
    path('', create_profile_page, name='create_profile_page'),
]
