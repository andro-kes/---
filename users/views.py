from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model, login, authenticate
from rest_framework.response import Response

User = get_user_model()

@api_view(['POST'])
def register(request):
    username = request.data['username']
    password = request.data['password']
    email = request.data['email']
    try:
        user = User.objects.create_user(username, password, email)
        user.save()
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({'message': 'Sign up succecfully', 'token': token.key})
    except Exception as e:
        return Response({'message': 'Registration failed', 'error': str(e)})
    
def register_page(request):
    return render(request, 'users/register.html')

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({'token': token.key, 'message': 'Login successful'})

def login_page(request):
    return render(request, 'users/login.html')
        
    
