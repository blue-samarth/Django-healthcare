# healthcare_project/doctors/urls.py
from django.urls import path
from .views import DoctorListCreateViews, DoctorDetailView, CurrentDoctorView

urlpatterns = [
    path('doctors/', DoctorListCreateViews.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('doctors/current/', CurrentDoctorView.as_view(), name='current-doctor'),
]
