from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
                       url(r'^$', Home.as_view(), name='home'),
                       url(r'^user/', include('registration.backends.simple.urls')),
url(r'^user/', include('django.contrib.auth.urls')),
                       url(r'^register/create/$', RegisterCreateView.as_view(), name='register_create'),
                       url(r'register/$', RegisterListView.as_view(), name='register_list'),
                      )