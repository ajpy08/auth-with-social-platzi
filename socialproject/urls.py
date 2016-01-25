"""socialproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Home URL
    url(
        r'^login/',
        TemplateView.as_view(template_name="home.html"),
        name="home"
    ),

    # Logout URL
    url(
        r'^users/logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': '/'},
        name="user-logout"
    ),
    # Python Social Auth URLs
	#url('', include('social.apps.django_app.urls', namespace='social')),
]
"""

"""Main URLs."""

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Administration site
    url(
        r'^admin/',
        include(admin.site.urls)
    ),

    # Python Social Auth
    url(
        '',
        include('social.apps.django_app.urls', namespace='social')
    ),

    # Home URL
    url(
        r'^login/',
        TemplateView.as_view(template_name="home.html"),
        name="home"
    ),

    # Logout URL
    url(
        r'^users/logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': '/login'},
        name="user-logout"
    ),
]
