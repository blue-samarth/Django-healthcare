# healthcare_project/patient_doctor_mapping/views.py
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer

class IsDoctorOrAdminStaff(permissions.BasePermission):
    """
    Custom permission to check if the user is a doctor or admin staff.
    """
    def has_permission(self, request, view):
        return request.user.is_doctor or request.user.is_admin_staff
    

class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctorOrAdminStaff]

    def create(self, request, *args, **kwargs):
        """
        Create a new PatientDoctorMapping instance.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def perform_create(self, serializer):
        """
        Create a new PatientDoctorMapping instance.
        """
        serializer.save(patient=self.request.user)

    
class MappingDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is used to retrieve, update and delete a PatientDoctorMapping instance.
    """
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctorOrAdminStaff]

    def get_object(self):
        """
        Retrieve a PatientDoctorMapping instance.
        """
        queryset = PatientDoctorMapping.objects.all()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
