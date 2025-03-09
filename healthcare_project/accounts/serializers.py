# heathcare_project/accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'is_patient', 'is_doctor', 'is_admin_staff']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email': 'Email is already in use'})
        
        try:
            validate_password(attrs['password'])
        except ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})

        return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # user = User(**validated_data)
        # if password:
        #     user.set_password(password)
        # user.save()
        if 'username' not in validated_data:
            validated_data['username'] = validated_data['email']
        user = User.objects.create_user(**validated_data, password=password)
        return user
