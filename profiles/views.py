from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Profiles
from .serializers import ProfileSerializer

class ProfileViewSet(ModelViewSet):
    queryset = Profiles.objects.all()
    serializer_class = ProfileSerializer
    
def create_profile_page(request):
    return render(request, 'profiles/create.html')