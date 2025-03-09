# healthcare_project/patients/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import PatientViewSet

urlpatterns = [
    path('patients/', PatientViewSet.as_view(), name='patients'),
    path('patients/<int:pk>/', PatientViewSet.as_view(), name='patient'),
    path('patients/<int:pk>/', PatientViewSet.as_view(), name='delete_patient'),
    path('patients/<int:pk>/', PatientViewSet.as_view(), name='update_patient'),
]
