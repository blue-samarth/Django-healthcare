# healthcare_project/doctors/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Doctor

User = get_user_model()

class UserInfoSerializer(serializers.ModelSerializer):
    """
    Serializer for basic user information
    """
    class Meta:
        model = User
        fields = ['id', 'name', 'email']
        read_only_fields = fields

class DoctorSerializer(serializers.ModelSerializer):
    """
    This class represents a Doctor serializer.
    """
    user_info = UserInfoSerializer(source='user', read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'user_info', 'name', 'specialty', 'experience', 'phone_number', 'created_at']
        extra_kwargs = {
            'user': {'read_only': True},
            'created_at': {'read_only': True}
        }

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Experience cannot be negative.")
        return value
    
    def create(self, validated_data):
        user = self.context['request'].user
        
        if not user.is_doctor:
            user.is_doctor = True
            user.save()
        
        if hasattr(user, 'doctor'):
            raise serializers.ValidationError("You are already a doctor.")
        
        doctor = Doctor.objects.create(user=user, **validated_data)
        return doctor
    
    def update(self, instance, validated_data):
        validated_data.pop('user', None)
        if 'experience' in validated_data:
            self.validate_age(validated_data['experience'])
        return super().update(instance, validated_data)
