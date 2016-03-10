"""lagentedice URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from despidos.views import *
from django.contrib.auth.decorators import login_required

admin.autodiscover()

urlpatterns = [
    # url(r'despidos/', include('despidos.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$',
        HomeView.as_view(),
        name='home'),
    url(r'^nuevo/$',
        login_required(NewDismissalView.as_view()),
        name='new_dismissal_view'),
    url(r'^(?P<pk>[0-9]+)/edit/$',
        login_required(EditDismissalView.as_view()),
        name='edit_dismissal_view'),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^(?P<pk>[0-9]+)/$', DismissalDetailView.as_view(),
        name='dismissal-detail'),

]
