from django.http.response import HttpResponse, Http404, HttpResponseForbidden
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView

from helpers.permissions import TeamPermission
from phase1.models import Category
from phase1.serializers import NewsSerializer


class GetURLsView(APIView):
    permission_classes = [TeamPermission]

    def get(self, request, *args, **kwargs):
        property = 'categorized_urls'
        if request.query_params.get('phase') == '3':
            property = 'uncategorized_urls'
        return HttpResponse(" ".join([str(url) for url in getattr(request.team, property).all()]))

class NewsView(TemplateView,APIView):
    permission_classes = [TeamPermission]
    template_name = 'phase1/news.html'
    def post(self,request,*args,**kwargs):
        text=request.POST.get('text')
        if(len(Category.objects.filter(category=text).all())==0):
            print("alksjdalskdjasd")
            return HttpResponseForbidden("No such category exists")
        news=Category.objects.get(category=text).news.all()
        x = NewsSerializer(news, many=True)
        return Response(x.data)


