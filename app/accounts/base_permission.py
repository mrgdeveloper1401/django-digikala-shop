from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
    
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or 
            request.user and request.user.is_authenticated
        )

    
class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_superuser:
            return True
        return False
