# healthcare_project/patients/views.py
from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.response import Response

from .models import Patient
from .serializers import PatientSerializer

# Create your views here.

class PatientViewSet(generics.GenericAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk, *args, **kwargs):
        patient = Patient.objects.get(pk=pk)
        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        patient = Patient.objects.get(pk=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
