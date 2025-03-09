# healthcare_project/accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('id', 'name', 'email', 'is_patient', 'is_doctor', 'is_admin_staff')
    list_filter = ('is_patient', 'is_doctor', 'is_admin_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_patient', 'is_doctor', 'is_admin_staff')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'email', 'password1', 'password2', 'is_patient', 'is_doctor', 'is_admin_staff'),
        }),
    )
    search_fields = ('name', 'email')
    ordering = ('email',)

admin.site.register(User, UserAdmin)

