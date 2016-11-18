from django.http.response import HttpResponse
from rest_framework.views import APIView

from helpers.permissions import TeamPermission


class Phase0View(APIView):
    permission_classes = [TeamPermission]

    def get(self, request, *args, **kwargs):
        return HttpResponse(request.team.text)