from rest_framework import serializers
from .models import Profiles
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    manager = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        models = Profiles
        fields = ('first_name', 'last_name', 'manager')
    
    def to_representation(self, instance):
        print(instance.manager)