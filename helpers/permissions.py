from rest_framework.permissions import BasePermission


class TeamPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_active:
            if getattr(request.user, 'team'):
                request.team = request.user.team
                return True
        return False