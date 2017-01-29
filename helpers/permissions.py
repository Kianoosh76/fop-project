from django.core.exceptions import PermissionDenied
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import BasePermission


class TeamPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_active:
            if hasattr(request.user, 'team'):
                request.team = request.user.team
                if request.method == 'POST' and not request.team.onsite_presentation:
                    raise ValidationError("It has been finished dear...! From now on, only "
                                          "memories remain!")
                return True
        return False


class AjaxPermission(BasePermission):
    def has_permission(self, request, view):
        return request.is_ajax()


class PermissionCheckerMixin:
    permission_classes = []

    def dispatch(self, request, *args, **kwargs):
        for permission_class in self.permission_classes:
            if not permission_class().has_permission(request, None):
                raise PermissionDenied("You do not have permission for this action")
        return super().dispatch(request, *args, **kwargs)
