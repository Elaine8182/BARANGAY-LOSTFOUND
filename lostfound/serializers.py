from rest_framework import serializers # type: ignore
from .models import Item  

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

from django.contrib.auth.models import User
from rest_framework import serializers # type: ignore

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
