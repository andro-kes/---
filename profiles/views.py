from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .serializers import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

User = get_user_model()

@api_view(['POST'])
def create_profile(request):
    request.data['manager'] = User.objects.get(username=request.data['manager']).pk
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'message': 'profile was created'})
    return Response({'error': 'Erorr'})
        
    
def create_profile_page(request):
    return render(request, 'profiles/create.html')