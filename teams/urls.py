from django.conf.urls import url

from teams.views import WelcomeView

urlpatterns=[
    url(r'^welcome/', WelcomeView.as_view(), name='welcome'),
]