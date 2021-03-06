from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.http.response import HttpResponseForbidden
from django.views.generic.list import ListView
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from helpers.background_color import BackgroundColorMixin
from helpers.permissions import TeamPermission, AjaxPermission
from teams.models import Team, Vote


class WelcomeView(APIView):
    permission_classes = [TeamPermission]

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hi {}! Your first request was sent successfully.".format(
            " and ".join([str(member.name) for member in request.team.members.all()])
        ))


class TeamsList(BackgroundColorMixin, ListView):
    model = Team
    template_name = 'teams/list.html'
    context_object_name = 'teams'
    ordering = '-votes'


class LikeView(APIView):
    permission_classes = [AjaxPermission, TeamPermission]

    def post(self, request, *args, **kwargs):
        member = get_object_or_404(request.team.members, id=int(request.POST.get('member', -1)))
        team = get_object_or_404(Team, id=int(request.POST.get('team', -1)))
        if team == request.team:
            raise PermissionDenied("You cannot like your own team")

        vote, created = Vote.objects.get_or_create(member=member, team=team)
        if not created:
            vote.valid ^= 1
            vote.save()
        team.refresh_from_db()
        vote.refresh_from_db()
        return Response({'votes': team.votes, 'valid': vote.valid})


def login_view(request, **kwargs):
    kwargs['extra_context'] = {'background_color': BackgroundColorMixin.get_color()}
    return auth_views.login(request, **kwargs)


def password_change_view(request, **kwargs):
    kwargs['extra_context'] = {'background_color': BackgroundColorMixin.get_color()}
    return auth_views.password_change(request, **kwargs)