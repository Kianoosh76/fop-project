"""fop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from phase0.views import Phase0View

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^phase0/', Phase0View.as_view(), name='phase0'),
    url(r'^news/', include('phase1.urls'), name='phase1'),
    url(r'^', include('teams.urls', namespace='team'))
]
