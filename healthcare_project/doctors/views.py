# healthcare_project/doctors/views.py
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from .models import Doctor
from .serializers import DoctorSerializer

class IsDoctor(permissions.BasePermission):
    """
    Custom permission to only allow doctors to access their own data.
    """

    # First we will make sure the user is authenticated and in order to get the doctor data either the user is a doctor or an admin staff member
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_doctor or request.user.is_admin_staff)

    
    # Then we will make sure the user is the owner of the doctor data
    def has_object_permission(self, request, view, obj):
        return request.user.is_admin_staff or obj.user == request.user

    
    # Get all the doctors for the admin staff
class DoctorListCreateViews(generics.ListCreateAPIView):
    """
    This class defines the views for listing and creating doctors
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsDoctor, permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_admin_staff:
            return Doctor.objects.all()
        return Doctor.objects.filter(user=self.request.user)

    # We will override the perform_create method to save the user as the current user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    This class defines the views for retrieving, updating and deleting doctors
    """
    serializer_class = DoctorSerializer
    permission_classes = [IsDoctor, permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Doctor.objects.all() if user.is_admin_staff else Doctor.objects.filter(user=user)

    
    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
class CurrentDoctorView(generics.RetrieveAPIView):
    """
    This class defines the views for retrieving, updating, Deleting the current doctor
    """
    serializer_class = DoctorSerializer
    permission_classes = [IsDoctor, permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Doctor, user=self.request.user)
