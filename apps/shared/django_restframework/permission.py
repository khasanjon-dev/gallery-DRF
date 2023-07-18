from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.is_superuser or user.is_staff or request.method in SAFE_METHODS:
            return True

        if user == obj or hasattr(obj, 'author') and obj.author == user:
            return True
        return False
