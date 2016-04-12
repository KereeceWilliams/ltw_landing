from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = patterns('',
                       url(r'^$', Home.as_view(), name='home'),
                       url(r'^user/', include('registration.backends.simple.urls')),
url(r'^user/', include('django.contrib.auth.urls')),
                       url(r'^team/delete/(?P<pk>\d+)/$', TeamDeleteView.as_view(), name='team_delete'),
                       url(r'^register/create/$', RegisterCreateView.as_view(), name='register_create'),
                       url(r'^donate/donate/$', DonateView.as_view(), name='donate'),
                       url(r'^team/create/$', login_required(TeamCreateView.as_view()), name='team_create'),
                       url(r'team/$', login_required(TeamListView.as_view()), name='team_list'),
                       url(r'^team/(?P<pk>\d+)/$', login_required(TeamDetailView.as_view()), name='team_detail'),
                       url(r'^team/update/(?P<pk>\d+)/$', login_required(TeamUpdateView.as_view()), name='team_update'),
                       url(r'^team/delete/(?P<pk>\d+)/$', login_required(TeamDeleteView.as_view()), name='team_delete'),
                       url(r'^team/(?P<pk>\d+)/member/create/$', login_required(MemberCreateView.as_view()), name='member_create'),
                       url(r'^team/(?P<team_pk>\d+)/member/update/(?P<member_pk>\d+)/$', login_required(MemberUpdateView.as_view()), name='member_update'),
                       url(r'^team/(?P<team_pk>\d+)/member/delete/(?P<member_pk>\d+)/$', login_required(MemberDeleteView.as_view()), name='member_delete'),
                       url(r'^user/(?P<slug>\w+)/$', login_required(UserDetailView.as_view()), name='user_detail'),
                       url(r'^user/update/(?P<slug>\w+)/$', login_required(UserUpdateView.as_view()), name='user_update'),
                       url(r'^user/delete/(?P<slug>\w+)/$', login_required(UserDeleteView.as_view()), name='user_delete'),
                       url(r'^search/$', login_required(SearchTeamListView.as_view()), name='search'),
               url(r'^vendor/create/$', VendorCreateView.as_view(), name='vendor_create'),        
                      )