from django.http import HttpResponse
from rest_framework.views import APIView

from helpers.permissions import TeamPermission


class WelcomeView(APIView):
    permission_classes = [TeamPermission]

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hi {}! Your first request was sent successfully.".format(
            " and ".join([str(member.name) for member in request.team.members.all()])
        ))
