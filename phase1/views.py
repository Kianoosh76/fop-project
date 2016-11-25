from django.http.response import HttpResponse
from rest_framework.views import APIView

from helpers.permissions import TeamPermission


class GetURLsView(APIView):
    permission_classes = [TeamPermission]

    def get(self, request, *args, **kwargs):
        property = 'categorized_urls'
        if request.query_params.get('phase') == '3':
            property = 'uncategorized_urls'
        return HttpResponse(" ".join([str(url) for url in getattr(request.team, property).all()]))