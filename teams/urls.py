from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from teams.views import WelcomeView, TeamsList, LikeView, login_view, password_change_view

urlpatterns= [
    url(r'^welcome/$', WelcomeView.as_view(), name='welcome'),
    url(r'^login/$', login_view, {'template_name': 'teams/login.html'}, name="login"),
    url(r'^logout/$', auth_views.logout,{'next_page': '/login/'}, name='logout'),
    url(r'password_change/$', password_change_view, {'template_name': 'teams/change_password.html','post_change_redirect':'/'}),
    url(r'^like/$', LikeView.as_view(), name='like'),
    url(r'^$', TeamsList.as_view(), name='list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)