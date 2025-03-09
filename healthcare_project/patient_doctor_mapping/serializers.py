# healthcare_project/patient_doctor_mapping/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import PatientDoctorMapping
from patients.models import Patient
from doctors.models import Doctor

User = get_user_model()

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    """
    This serializer is used to serialize the PatientDoctorMapping model.
    """

    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())


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
        user = self.context['request'].user
        # If the user is a patient, enforce that they are the patient in the mapping.
        if user.is_patient and validated_data.get('patient') != user:
            raise serializers.ValidationError("Patients can only create mappings for themselves.")
        # If the user is a doctor, enforce that they are the doctor in the mapping.
        if user.is_doctor and validated_data.get('doctor') != user:
            raise serializers.ValidationError("Doctors can only create mappings for themselves.")
        # Optionally, check if a mapping already exists.
        if PatientDoctorMapping.objects.filter(patient=validated_data.get('patient'),
                                                doctor=validated_data.get('doctor')).exists():
            raise serializers.ValidationError("This mapping already exists.")
        return PatientDoctorMapping.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        """
        Update a PatientDoctorMapping instance.
        """
        user = self.context['request'].user
        if user != instance.patient and user != instance.doctor:
            raise serializers.ValidationError("You are not authorized to update this mapping.")
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()
        return instance

