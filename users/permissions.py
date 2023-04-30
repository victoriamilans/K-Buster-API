from rest_framework import permissions
from rest_framework.views import Request, View


class IsEmployeeOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_employee
        )


class IsAuthenticatedandEmployeePermission(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, user):
        return request.user.is_employee or user == request.user
