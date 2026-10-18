from rest_framework.permissions import BasePermission


class IsLoggedIn(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated


class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
