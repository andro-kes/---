from rest_framework import serializers
from .models import Profiles
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = ('first_name', 'last_name', 'manager')
        
        
            
