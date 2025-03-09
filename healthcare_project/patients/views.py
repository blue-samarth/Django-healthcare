# healthcare_project/patients/views.py
from django.shortcuts import get_object_or_404
from rest_framework import status, generics, permissions
from rest_framework.response import Response

from .models import Patient
from .serializers import PatientSerializer

# Create your views here.

class IsDoctorOrAdminStaff(permissions.BasePermission):
    """
    This permission class checks if the user is a doctor or an admin staff
    """
    def has_permission(self, request, view):
        return (request.user.is_doctor or request.user.is_admin_staff) and (request.user.is_authenticated)


class PatientListCreateView(generics.ListCreateAPIView):
    """
    This view is for listing and creating patients
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_doctor or user.is_admin_staff:
            return Patient.objects.all()
        return Patient.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save()

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is for retrieving, updating and deleting patients
    """
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_doctor or user.is_admin_staff:
            return Patient.objects.all()
        return Patient.objects.filter(user=user)

    def get_object(self):
        object = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, object)
        return object
    

class CurrentPatientView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is for retrieving, updating and deleting the current patient
    """
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        object = get_object_or_404(Patient, user=self.request.user)
        return object
