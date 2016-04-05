from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
                       url(r'^$', Home.as_view(), name='home'),
                       url(r'^user/', include('registration.backends.simple.urls')),
url(r'^user/', include('django.contrib.auth.urls')),
                       url(r'^register/create/$', RegisterCreateView.as_view(), name='register_create'),
                       url(r'^donate/donate/$', DonateView.as_view(), name='donate'),
                       url(r'^team/create/$', TeamCreateView.as_view(), name='team_create'),
                       url(r'team/$', TeamListView.as_view(), name='team_list'),
                       url(r'^team/(?P<pk>\d+)/$', TeamDetailView.as_view(), name='team_detail'),
                       url(r'^team/update/(?P<pk>\d+)/$', TeamUpdateView.as_view(), name='team_update'),
                      )