from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('api/register/', views.register, name='register'),
    path('register', views.register_page, name='register_page'),
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('', views.login_page, name='login_page'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]
