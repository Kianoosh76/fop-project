from django.conf.urls import url

from phase1.views import GetURLsView, NewsView, SearchView

urlpatterns = [
    url(r'^get-urls/$', GetURLsView.as_view(), name='get-urls'),
    url(r'^$', NewsView.as_view(), name='news'),
]
