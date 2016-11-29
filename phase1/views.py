from django.http.response import HttpResponse, Http404, HttpResponseForbidden
from django.views.generic import TemplateView
from rest_framework.generics import get_object_or_404, GenericAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from helpers.permissions import TeamPermission, PermissionCheckerMixin, AjaxPermission
from phase1.models import Category
from phase1.serializers import NewsSerializer


class GetURLsView(APIView):
    permission_classes = [TeamPermission]

    def get(self, request, *args, **kwargs):
        property = 'categorized_urls'
        if request.query_params.get('phase') == '3':
            property = 'uncategorized_urls'
        return HttpResponse(" ".join([str(url) for url in getattr(request.team, property).all()]))


class SearchView(PermissionCheckerMixin, TemplateView):
    permission_classes = [TeamPermission]
    template_name = 'phase1/news.html'


class NewsView(ListCreateAPIView):
    permission_classes = [AjaxPermission, TeamPermission]
    serializer_class = NewsSerializer

    def get_queryset(self):
        return self.request.team.news

    def filter_queryset(self, queryset):
        category = self.request.query_params.get('category').lower()
        is_cat = self.request.query_params.get('isCat')
        return queryset.filter(categorized=is_cat != 'false', categories__category__in=[category])

    def perform_create(self, serializer):
        categories = self.request.data.get('categories')
        category_objects = []
        for category in categories:
            category_object, _ = Category.objects.get_or_create(category=category.lower())
            category_objects.append(category_object)

        instance = serializer.save()

        instance.categories = category_objects