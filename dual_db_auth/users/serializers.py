from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')  
        user = User(**validated_data)  
        user.set_password(password)  
        user.save(using='write_db')  # Save to write_db
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        # Save to write_db
        product = Product.objects.using('write_db').create(**validated_data)
        return product
