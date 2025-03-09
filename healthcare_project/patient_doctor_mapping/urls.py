# healthcare_project/patient_doctor_mapping/urls.py
from django.urls import path
from .views import PatientDoctorMappingViewSet, MappingDetailView

urlpatterns = [
    path('mappings/', PatientDoctorMappingViewSet.as_view({'get': 'list', 'post': 'create'}), name='mappings'),
    path('mappings/<int:pk>/', MappingDetailView.as_view(), name='mapping-detail'),
]
