from django.contrib.auth.models import User
from rest_framework import serializers
from api import models

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Market
        fields = '__all__'

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: User
        fields = 'username', 'password'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user