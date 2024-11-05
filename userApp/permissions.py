# userApp/permissions.py

from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow admins to access certain views.
    """
    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin'

class IsUserOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow the user themselves or admins to access certain views.
    """
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.role == 'admin'
