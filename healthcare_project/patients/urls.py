# healthcare_project/patients/urls.py
from django.urls import path
from .views import PatientListCreateView, PatientDetailView, CurrentPatientView

urlpatterns = [
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('my-profile/', CurrentPatientView.as_view(), name='current-patient'),
]
