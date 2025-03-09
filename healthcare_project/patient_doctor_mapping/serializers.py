# healthcare_project/patient_doctor_mapping/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import PatientDoctorMapping

User = get_user_model()

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    """
    This serializer is used to serialize the PatientDoctorMapping model.
    """
    patient = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'
        extra_kwargs = {
            'assigned_at': {'read_only': True},
            'created_at': {'read_only': True},
        }
    
    def validate(self, data):
        """
        Check if the patient is a patient and the doctor is a doctor.
        """
        patient = data['patient']
        doctor = data['doctor']
        if not patient.is_patient:
            raise serializers.ValidationError('The patient must be a patient.')
        if not doctor.is_doctor:
            raise serializers.ValidationError('The doctor must be a doctor.')
        return data
    
    def create(self, validated_data):
        """
        Create a new PatientDoctorMapping instance.
        """
        user = self.context['request'].user

        if user != validated_data['patient'] or user != validated_data['doctor']:
            raise serializers.ValidationError('The patient and doctor must be the authenticated user.')
        
        if hasattr(user, 'patient_doctor_mapping'):
            raise serializers.ValidationError('This appointment already exists.')
        
        mapping = PatientDoctorMapping.objects.create(**validated_data)
        return mapping
    
    def update(self, instance, validated_data):
        """
        Update a PatientDoctorMapping instance.
        """
        user = self.context['request'].user

        if user != instance.patient or user != instance.doctor:
            raise serializers.ValidationError('The patient and doctor must be the authenticated user.')
        
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()
        return instance
