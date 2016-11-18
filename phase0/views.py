from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.views import APIView

from helpers.permissions import TeamPermission


class Phase0View(APIView):
    permission_classes = [TeamPermission]

    def get(self, request, *args, **kwargs):
        return HttpResponse(request.team.text)


class WelcomeView(APIView):
    permission_classes= [TeamPermission]

    def get(self,request,*args,**kwargs):
        return HttpResponse(" and ".join([str(member.name) for member in request.user.team.members.all()])+" your first request is sent successfully.")
