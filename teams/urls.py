from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import reverse

from teams.views import WelcomeView

urlpatterns= [
    url(r'^welcome/$', WelcomeView.as_view(), name='welcome'),
    url(r'^login/$', auth_views.login,{'template_name': 'teams/login.html'}, name="login"),
    url(r'^logout/$', auth_views.logout,{'next_page': '/login/'}, name='logout'),
]