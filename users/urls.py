from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', views.register, name='register'),
    path('register_page', views.register_page, name='register_page'),
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('', views.login_page, name='login_page'),
]
