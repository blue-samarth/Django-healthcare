# healthcare_project/patients/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Patient

User = get_user_model()

class UserInfoSerializer(serializers.ModelSerializer):
    """
    Serializer for basic user information
    """
    class Meta:
        model = User
        fields = ['id', 'name', 'email']
        read_only_fields = fields


class PatientSerializer(serializers.ModelSerializer):
    """
    Serializer for the patient model in the database
    """
    user_info = UserInfoSerializer(source='user', read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'user', 'user_info', 'age', 'address', 'phone_number', 'blood_group', 'created_at']
        extra_kwargs = {
            'user': {'read_only': True},
            'created_at': {'read_only': True}
        }

    def validate_age(self, value):
        if not (0 <= value <= 120):
            raise serializers.ValidationError("Age must be between 0 and 120 years.")
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        
        if not user.is_patient:
            user.is_patient = True
            user.save()
        
        if hasattr(user, 'patient'):
            raise serializers.ValidationError('Patient Profile Already Exists for this User')

        patient = Patient.objects.create(user=user, **validated_data)
        return patient
    
    def update(self, instance, validated_data):
        validated_data.pop('user', None)
        if 'age' in validated_data:
            self.validate_age(validated_data['age'])
        return super().update(instance, validated_data)
