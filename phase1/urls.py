from django.conf.urls import url

from phase1.views import GetURLsView

urlpatterns = [
    url(r'^get-urls/', GetURLsView.as_view(), name='get-urls'),
]
