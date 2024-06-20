from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['id'] = user.id
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['id'] = self.user.id
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['image', 'username', 'password', 'email', 'first_name', 'last_name', 'phone_number', 'is_driver', 'car_model', 'car_color']

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("This field may not be blank.")

        # Exclude the current user from the query.
        user = self.instance
        if user and user.email == value:
            return value

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data.get('username', ''),
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_driver=validated_data.get('is_driver', False),
            car_model=validated_data.get('car_model', None),
            car_color=validated_data.get('car_color', None),
            image=validated_data.get('image', None),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        return super().update(instance, validated_data)