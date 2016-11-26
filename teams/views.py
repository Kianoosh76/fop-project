from django.http import HttpResponse
from django.views.generic.list import ListView
from rest_framework.views import APIView

from helpers.permissions import TeamPermission, PermissionCheckerMixin
from teams.models import Team


class WelcomeView(APIView):
    permission_classes = [TeamPermission]

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hi {}! Your first request was sent successfully.".format(
            " and ".join([str(member.name) for member in request.team.members.all()])
        ))


class TeamsList(ListView):
    model = Team
    template_name = 'teams/list.html'
    context_object_name = 'teams'