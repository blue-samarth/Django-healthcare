# healthcare_project/patients/serializers.py
from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'user', 'age', 'address', 'phone_number', 'created_at']
        extra_kwargs = {
            'user': {'read_only': True},
            'created_at': {'read_only': True}
        }

    def create(self, validated_data):
        user = self.context['request'].user
        patient = Patient.objects.create(user=user, **validated_data)
        return patient
