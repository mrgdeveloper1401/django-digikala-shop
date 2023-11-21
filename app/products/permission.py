from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
    
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
           return True
        return False