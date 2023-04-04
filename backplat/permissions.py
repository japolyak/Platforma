from rest_framework import permissions


class IsOwnerOrAdminUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if not obj.teacher == request.user:
            return bool(request.user.is_staff)

        return obj.teacher == request.user
