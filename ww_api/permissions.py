from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Checks to see if user is owner of the profile"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
