# healthcare_project/doctors/urls.py
from django.urls import path
from .views import DoctorListcreateViews, DocterDetailedView, CurrentDoctorview

urlpatterns = [
    path('doctors/', DoctorListcreateViews.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DocterDetailedView.as_view(), name='doctor-detail'),
    path('doctors/current/', CurrentDoctorview.as_view(), name='current-doctor'),
]
